import sounddevice as sd
import numpy as np
import os

from app.notes import note_to_frequency
from app.generator import generate_melody
from scipy.io.wavfile import write

SAMPLE_RATE = 44100

def generate_wave(frequency: float, duration: float, volume: float = 0.04) -> np.ndarray:
    """
    Generate a square wave for a given frequency and duration.

    Args:
        frequency (float): Frequency of the wave in Hz.
        duration (float): Duration of the wave in seconds.
        volume (float): Volume of the wave (0.0 to 1.0).

    Returns:
        np.ndarray: Array of wave samples.
    """
    if frequency == 0:
        return np.zeros(int(SAMPLE_RATE * duration), dtype=np.float32)
    
    t = np.linspace(0, duration, int(SAMPLE_RATE * duration), endpoint=False)
    wave = volume * np.sign(np.sin(2 * np.pi * frequency * t))
    return wave.astype(np.float32)

def play_note(frequency: float, duration: float, volume: float = 0.04):
    """
    Play a note with the given frequency and duration.

    Args:
        frequency (float): Frequency of the note in Hz.
        duration (float): Duration of the note in seconds.
        volume (float): Volume of the note (0.0 to 1.0).
    """
    wave = generate_wave(frequency, duration, volume)
    sd.play(wave, samplerate=SAMPLE_RATE)
    sd.wait()

def play_melody(melody: list, volume: float = 0.04):
    """
    Play a melody with the given melody and volume.

    Args:
        melody (list): List of notes to play.
        volume (float): Volume of the melody (0.0 to 1.0).
    """
    full_wave = _generate_full_wave(melody, volume)
    sd.play(full_wave, samplerate=SAMPLE_RATE)
    sd.wait()

def save_melody(melody: list, filename="melody.wav", volume: float = 0.04):
    """
    Save a melody to a WAV file.

    Args:
        melody (list): List of notes to save.
        filename (str): Name of the file to save.
        volume (float): Volume of the melody (0.0 to 1.0).
    """
    full_wave = np.concatenate([
        generate_wave(note_to_frequency(note), duration, volume)
        for note, duration in melody
    ])

    base_dir = os.path.dirname(os.path.dirname(__file__))
    wav_path = os.path.join(base_dir, "generated_melodies")
    os.makedirs(wav_path, exist_ok=True)

    full_path = os.path.join(wav_path, filename)
    write(full_path, SAMPLE_RATE, full_wave)
    
def _generate_full_wave(melody: list, volume: float = 0.04) -> np.ndarray:
    """
    Generate a full wave from a melody.

    Args:
        melody (list): List of notes to generate.
        volume (float): Volume of the melody (0.0 to 1.0).

    Returns:
        np.ndarray: Array of wave samples.
    """
    return np.concatenate([
        generate_wave(note_to_frequency(note), duration, volume) for note, duration in melody
    ])
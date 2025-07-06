import sounddevice as sd
import numpy as np
import os

from app.notes import note_to_frequency
from app.generator import generate_melody
from scipy.io.wavfile import write

SAMPLE_RATE = 44100

def generate_wave(frequency: float, duration: float, volume: float = 0.05) -> np.ndarray:
    if frequency == 0:
        return np.zeros(int(SAMPLE_RATE * duration), dtype=np.float32)
    
    t = np.linspace(0, duration, int(SAMPLE_RATE * duration), endpoint=False)
    wave = volume * np.sign(np.sin(2 * np.pi * frequency * t))
    return wave.astype(np.float32)

def play_note(frequency: float, duration: float, volume: float = 0.05):
    wave = generate_wave(frequency, duration, volume)
    sd.play(wave, samplerate=SAMPLE_RATE)
    sd.wait()

def play_melody(melody: list, volume: float = 0.05):
    full_wave = _generate_full_wave(melody, volume)
    sd.play(full_wave, samplerate=SAMPLE_RATE)
    sd.wait()

def save_melody(melody: list, filename="melody.wav", volume: float = 0.05):
    full_wave = np.concatenate([
        generate_wave(note_to_frequency(note), duration, volume)
        for note, duration in melody
    ])

    base_dir = os.path.dirname(os.path.dirname(__file__))
    wav_path = os.path.join(base_dir, "wav")
    os.makedirs(wav_path, exist_ok=True)

    full_path = os.path.join(wav_path, filename)
    print(full_path)
    write(full_path, SAMPLE_RATE, full_wave)
    
def _generate_full_wave(melody: list, volume: float = 0.05) -> np.ndarray:
    return np.concatenate([
        generate_wave(note_to_frequency(note), duration, volume) for note, duration in melody
    ])
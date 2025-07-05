import sounddevice as sd
import numpy as np
import matplotlib.pyplot as plt

SAMPLE_RATE = 44100

def generate_wave(frequency: float, duration: float, volume: float = 0.5) -> np.ndarray:
    if frequency == 0:
        return np.zeros(int(SAMPLE_RATE * duration), dtype=np.float32)
    
    t = np.linspace(0, duration, int(SAMPLE_RATE * duration), endpoint=False)
    wave = volume * np.sign(np.sin(2 * np.pi * frequency * t))
    return wave.astype(np.float32)
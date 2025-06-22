import sounddevice as sd
import numpy as np

SAMPLE_RATE = 44100

def play_note(frequency: float, duration: float, volume: float = 0.5):
    if frequency <= 0:
        sd.sleep(int(duration * 1000))
        return
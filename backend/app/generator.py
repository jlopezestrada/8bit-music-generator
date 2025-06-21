import random
from app.notes import octave_notes_frequency

DURATIONS = [0.25, 0.5, 1.0]

def generate_melody(length: int = 5, start_octave: int = 4, end_octave: int = 5) -> list:
    notes = list(octave_notes_frequency(start_octave=start_octave, end_octave=end_octave).keys())
    return [(random.choice(notes), random.choice(DURATIONS)) for _ in range(length)]

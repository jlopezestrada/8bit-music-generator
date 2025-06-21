A4_FREQ = 440.0
A4_INDEX = 9 + 12 * 4 # index of the A4 in the chromatic scale (12 semitones per scale, 4 octaves, 9th note)

SEMITONES = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']

def octave_notes_frequency(start_octave: int = 4, end_octave: int = 5) -> list:
    """
    Based on function f = 440 \times 2^{\frac{n}{12}}
    """
    note_freqs = {}
    for octave in range(start_octave, end_octave + 1):
        for i, note in enumerate(SEMITONES):
            index = i + 12 * octave
            n = index - A4_INDEX
            freq = A4_FREQ * 2 ** (n / 12)
            note_name = f"{note}{octave}"
            note_freqs[note_name] = round(freq, 2)
    return note_freqs 

def note_to_frequency(note_str: str) -> float:
    _, octave = _parse_note_string(note_str)
    octave_frequencies = octave_notes_frequency(start_octave=octave, end_octave=octave)
    return octave_frequencies[note_str]

def _parse_note_string(note_str: str) -> tuple:
    for i in [2, 1]:
        note = note_str[:i]
        if note in SEMITONES:
            octave_str = note_str[i:]
            if octave_str.isdigit():
                return note, int(octave_str)
            break
    raise ValueError(f"Invalid note format: {note_str}")

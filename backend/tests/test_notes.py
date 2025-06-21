import pytest
from app.notes import note_to_frequency, octave_notes_frequency, _parse_note_string

def test_parse_note_string_valid():
    """
    Test that valid note strings (note + octave) are parsed correctly
    into their corresponding note and octave tuple.
    """
    assert _parse_note_string("C4") == ("C", 4)
    assert _parse_note_string("A#3") == ("A#", 3)
    assert _parse_note_string("G#7") == ("G#", 7)
    assert _parse_note_string("D5") == ("D", 5)
    assert _parse_note_string("C#0") == ("C#", 0)
    assert _parse_note_string("B8") == ("B", 8)

def test_parse_note_string_invalid():
    """
    Test that invalid note strings raise ValueError.
    Includes bad formats, unknown notes, or missing octaves.
    """
    with pytest.raises(ValueError):
        _parse_note_string("H4")
    with pytest.raises(ValueError):
        _parse_note_string("Aaaa5")
    with pytest.raises(ValueError):
        _parse_note_string("4C")
    with pytest.raises(ValueError):
        _parse_note_string("C#")
    with pytest.raises(ValueError):
        _parse_note_string("")
    with pytest.raises(ValueError):
        _parse_note_string("##5")

def test_note_to_frequency_values():
    """
    Test that known notes return expected frequency values.
    Rounded values are compared for common notes across octaves.
    """
    assert note_to_frequency("A4") == 440.0
    assert note_to_frequency("C4") == 261.63
    assert note_to_frequency("C5") == 523.25
    assert note_to_frequency("E4") == 329.63
    assert note_to_frequency("G3") == 196.0
    assert note_to_frequency("B2") == 123.47

def test_note_to_frequency_out_of_range_handling():
    """
    Test that invalid or incomplete notes raise ValueError when
    passed to note_to_frequency().
    """
    with pytest.raises(ValueError):
        note_to_frequency("C#")  # no octave
    with pytest.raises(ValueError):
        note_to_frequency("D#-1")  # negative octave

def test_octave_notes_frequency_range():
    """
    Test that octave_notes_frequency returns exactly 12 semitones
    for a single octave and includes specific expected notes.
    """
    freqs = octave_notes_frequency(4, 4)
    assert "C4" in freqs
    assert "B4" in freqs
    assert len(freqs) == 12
    assert freqs["A4"] == 440.0

def test_octave_notes_frequency_multioctave():
    """
    Test that octave_notes_frequency returns all notes across
    multiple octaves, with expected count and key coverage.
    """
    freqs = octave_notes_frequency(3, 5)
    assert "C3" in freqs
    assert "C4" in freqs
    assert "C5" in freqs
    assert "B5" in freqs
    assert len(freqs) == 12 * 3

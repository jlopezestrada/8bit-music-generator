from pydantic import BaseModel

class MelodyRequest(BaseModel):
    length: int = 50
    start_octave: int = 3
    end_octave: int = 5

class MelodyResponse(BaseModel):
    song_id: str
    notes: list
    wav_url: str
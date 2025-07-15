from fastapi import FastAPI
from api_models import MelodyRequest, MelodyResponse
from app.generator import generate_melody
from app.player import save_melody
import uvicorn
import uuid
import os

app = FastAPI()

@app.post("/generate", response_model=MelodyResponse)
def generate_song(params: MelodyRequest):
    melody = generate_melody(
        length=params.length,
        start_octave=params.start_octave,
        end_octave=params.end_octave
    )
    song_id = str(uuid.uuid4())

    save_melody(melody=melody, filename=f"{song_id}.wav")

    return MelodyResponse(
        song_id=song_id,
        notes=melody,
        wav_url=f"generated_melodies/{song_id}.wav"
    )

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
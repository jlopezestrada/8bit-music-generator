from app.generator import generate_melody
from app.player import save_melody

def main():
    print("8-Bit Music Generator")
    melody = generate_melody(length=25, start_octave=3, end_octave=5)

    for note, duration in melody:
        print(f" - {note}, duration: {duration}s")

    save_melody(melody, volume=0.05)

if __name__ == "__main__":
    main()
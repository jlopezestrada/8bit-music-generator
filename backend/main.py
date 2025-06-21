# TODO
from app.generator import generate_melody

def main():
    print("8-Bit Music Generator")

    melody = generate_melody(length=150, start_octave=3, end_octave=5)
    print("Generated melody:")
    for note_name, duration in melody:
        print(f" - {note_name}, duration: {duration}s")

if __name__ == "__main__":
    main()
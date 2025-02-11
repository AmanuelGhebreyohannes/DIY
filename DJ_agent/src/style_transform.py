import librosa
import pyrubberband as rb
import soundfile as sf

def transform_to_house(file_path, output_path="output_house.wav"):
    # Load audio
    y, sr = librosa.load(file_path)

    # Adjust tempo to house music range (120-130 BPM)
    y_stretched = rb.time_stretch(y, sr, 1.15)  # Increase tempo by 20%

    # Save transformed audio
    sf.write(output_path, y_stretched, sr)
    print(f"Transformed audio saved to {output_path}")

if __name__ == "__main__":
    transform_to_house("../data/song.mp3")
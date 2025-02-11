import librosa

def analyze_audio(file_path):
    # Load audio file
    y, sr = librosa.load(file_path)

    # Extract BPM and beats
    bpm, beats = librosa.beat.beat_track(y=y, sr=sr)
    print(f"BPM: {bpm}")

    # Extract key (chroma features)
    chroma = librosa.feature.chroma_cqt(y=y, sr=sr)
    print(f"Chroma Features: {chroma}")

    return bpm, beats, chroma

if __name__ == "__main__":
    analyze_audio("../data/song.mp3")
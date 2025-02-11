import pyaudio
import librosa
import numpy as np

def play_audio(file_path):
    # Load audio
    y, sr = librosa.load(file_path, sr=None)

    # Initialize PyAudio
    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paFloat32, channels=1, rate=sr, output=True)

    # Play audio
    stream.write(y.astype(np.float32).tobytes())
    stream.stop_stream()
    stream.close()
    p.terminate()

if __name__ == "__main__":
    play_audio("output_house.wav")
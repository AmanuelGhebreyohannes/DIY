import librosa
import pyrubberband as rb
import soundfile as sf
import numpy as np
from scipy.io.wavfile import write

def generate_kick_drum(duration, sr, frequency=50, decay=0.1):
    """Generate a simple kick drum sound."""
    t = np.linspace(0, duration, int(sr * duration), False)
    kick = np.sin(2 * np.pi * frequency * t) * np.exp(-t / decay)
    return kick

def add_four_on_the_floor(y, sr, bpm):
    """Add a four-on-the-floor beat to the audio."""
    # Calculate the interval between kicks (in samples)
    beat_interval = int((60 / bpm) * sr)

    # Generate a kick drum sound
    kick_duration = 0.1  # 100ms kick drum
    kick = generate_kick_drum(kick_duration, sr)

    # Create a beat track with the same length as the input audio
    beat_track = np.zeros_like(y)
    for i in range(0, len(y), beat_interval):
        end = min(i + len(kick), len(y))
        beat_track[i:end] += kick[:end - i]

    return beat_track

def generate_sine_wave(frequency, duration, sr, amplitude=0.1):
    """Generate a sine wave."""
    t = np.linspace(0, duration, int(sr * duration), False)
    return amplitude * np.sin(2 * np.pi * frequency * t)

def add_synth_melody(y, sr, bpm):
    """Add a simple synth melody to the audio."""
    # Define a simple melody (frequencies in Hz)
    melody_notes = [440, 554, 659, 554]  # A4, C#5, E5, C#5
    note_duration = (60 / bpm) / 2  # Half-beat notes

    # Generate the melody with the same length as the input audio
    melody_track = np.zeros_like(y)
    for i, freq in enumerate(melody_notes):
        start = int(i * note_duration * sr)
        end = int((i + 1) * note_duration * sr)
        if end > len(y):  # Ensure we don't exceed the length of the audio
            break
        note = generate_sine_wave(freq, note_duration, sr)
        melody_track[start:end] += note[:end - start]

    return melody_track

def normalize_audio(y):
    """Normalize audio to prevent clipping."""
    return y / np.max(np.abs(y))

def transform_to_house(file_path, output_path="output_house.wav"):
    # Load audio
    y, sr = librosa.load(file_path)

    # Adjust tempo to house music range (120-130 BPM)
    target_bpm = 128  # Typical house music BPM
    y_stretched = rb.time_stretch(y, sr, target_bpm / librosa.beat.tempo(y=y, sr=sr)[0])

    # Add a four-on-the-floor beat
    beat_track = add_four_on_the_floor(y_stretched, sr, target_bpm)

    # Add a synth melody
    melody_track = add_synth_melody(y_stretched, sr, target_bpm)

    # Mix all tracks
    mixed_audio = y_stretched + beat_track + melody_track

    # Normalize the mixed audio
    mixed_audio = normalize_audio(mixed_audio)

    # Save transformed audio
    sf.write(output_path, mixed_audio, sr)
    print(f"Transformed audio saved to {output_path}")


if __name__ == "__main__":
    transform_to_house("../data/song.mp3")
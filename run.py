import librosa
import numpy as np

def get_notes_from_audio_file(file_path):
    # Load the audio file
    y, sr = librosa.load(file_path)

    # Perform a Short-Time Fourier Transform (STFT) to convert the audio from the time domain to the frequency domain
    D = librosa.stft(y)

    # Compute the magnitude spectrogram
    S = np.abs(D)

    # Identify the pitches
    pitches, magnitudes = librosa.piptrack(S=S, sr=sr)

    # Filter out pitches with low magnitudes
    pitches = pitches[magnitudes > np.median(magnitudes)]

    # Convert the pitches to note names
    notes = [librosa.hz_to_note(p) for p in pitches]

    return notes

# Example usage
recording_path = "./recording.wav"
notes = get_notes_from_audio_file(recording_path)
print(notes)
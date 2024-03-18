from midiutil import MIDIFile
import librosa
import numpy as np

def audio_to_piano_audio(file_path):
    # Load the audio file and resample it to 44.1 kHz
    y, sr = librosa.load(file_path, sr=44100)

    # Skip short files
    if len(y) < 2048:
        print(f"File {file_path} is too short for Fourier transform")
        return []

    # Detect the onset frames of the notes
    onset_frames = librosa.onset.onset_detect(y=y, sr=sr)

    # Convert the onset frames to times
    onset_times = librosa.frames_to_time(onset_frames, sr=sr)

    # Compute the short-time Fourier transform with a dynamically adjusted n_fft
    n_fft = min(2048, len(y))
    D = np.abs(librosa.stft(y, n_fft=n_fft))

    # Identify the pitches and their magnitudes with adjusted n_fft
    pitches, magnitudes = librosa.piptrack(y=y, sr=sr)

    # Create a new MIDI file with one track
    midi = MIDIFile(1)

    # Set the instrument (MIDI program) for the track (0 is Acoustic Grand Piano)
    midi.addProgramChange(0, 0, 0, 0)

    # Add the notes to the MIDI file
    for i, onset_time in enumerate(onset_times):
        # Find the pitch and magnitude at the onset time
        onset_sample = int(onset_time * sr / 512)  # Use the hop length of the STFT
        onset_pitch = pitches[:, onset_sample].argmax()
        onset_magnitude = magnitudes[onset_pitch, onset_sample]

        # Skip notes with zero pitch
        if onset_pitch <= 0:
            continue

        # Convert the pitch to a MIDI note and round to the nearest integer
        onset_note = int(round(librosa.hz_to_midi(onset_pitch)))

        # If onset_magnitude is an array, take the maximum magnitude
        if isinstance(onset_magnitude, np.ndarray):
            onset_magnitude = onset_magnitude.max()

        # Ensure the volume is within the valid MIDI range
        volume = int(onset_magnitude * 100)
        volume = max(0, min(volume, 127))

        # Add the note to the MIDI file
        midi.addNote(0, 0, onset_note, onset_time, 1, volume)

    return onset_times

# Example usage
recording_path = "./recording.wav"
onset_times = audio_to_piano_audio(recording_path)
print(onset_times)
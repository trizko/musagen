from midi2audio import FluidSynth

def midi_to_wav(midi_file, soundfont_file, output_file):
    # Create a FluidSynth instance
    fs = FluidSynth(soundfont_file)

    # Convert the MIDI file to a WAV file
    fs.midi_to_audio(midi_file, output_file)

# Example usage
midi_file = "./super_mario_64_medley.mid"
soundfont_file = "./chorium.sf2"
output_file = "./output.wav"

midi_to_wav(midi_file, soundfont_file, output_file)
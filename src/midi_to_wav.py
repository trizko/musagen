import argparse
from midi2audio import FluidSynth

def midi_to_wav(midi_file, soundfont_file, output_file):
    fs = FluidSynth(soundfont_file)
    fs.midi_to_audio(midi_file, output_file)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Convert MIDI to WAV')
    parser.add_argument('midi_file', help='Input MIDI file')
    parser.add_argument('soundfont_file', help='SoundFont file')
    parser.add_argument('output_file', help='Output WAV file')
    args = parser.parse_args()

    midi_to_wav(args.midi_file, args.soundfont_file, args.output_file)
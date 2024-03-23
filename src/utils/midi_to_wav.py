import argparse
from midi2audio import FluidSynth

def midi_to_wav(midi_file, soundfont_file, output_file):
    fs = FluidSynth(soundfont_file)

    fs.midi_to_audio(midi_file, output_file)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Convert MIDI to WAV')
    parser.add_argument('--midi', '-m', required=True, help='Input MIDI file')
    parser.add_argument('--soundfont', '-s', help='SoundFont file (defaults to fluidsynth `default.sf2`)', default='')
    parser.add_argument('output_file', nargs='?', help='Output WAV file (defaults `to output.wav`)', default='output.wav')
    args = parser.parse_args()

    midi_to_wav(args.midi, args.soundfont, args.output_file)
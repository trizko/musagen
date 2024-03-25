import argparse
from music21 import converter

def midi_to_text(midi_file, output_file):
    abc_stream = converter.parse(midi_file, format='midi')
    abc_stream.write('text', fp=output_file)
    
    print(f"text file saved as {output_file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Convert MIDI to Text')
    parser.add_argument('--midi', '-m', required=True, help='Input MIDI file')
    parser.add_argument('output_file', nargs='?', help='Output WAV file (defaults `to output.txt`)', default='output.txt')
    args = parser.parse_args()

    midi_to_text(args.midi, args.output_file)
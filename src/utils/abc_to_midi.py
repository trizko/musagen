import argparse
from music21 import converter

def abc_to_midi(abc_file_path, output_file):
    abc_stream = converter.parse(abc_file_path)
    
    abc_stream.write('midi', fp=output_file)
    
    print(f"MIDI file saved as {output_file}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Convert ABC notation file to a MIDI file')
    parser.add_argument('--abc', '-a', required=True, help='Input .abc file path')
    parser.add_argument('output_file', nargs='?', help='Output .midi file path (defaults `to output.midi`)', default='output.midi')
    args = parser.parse_args()

    abc_to_midi(args.abc, args.output_file)

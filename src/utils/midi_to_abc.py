import argparse
import music21

def midi_to_abc(midi_file_path, abc_file_path):
    midi = music21.converter.parse(midi_file_path)

    abc_header = "X:1\nT:Untitled\nM:4/4\nK:C\n"
    notes = []
    for note in midi.flatten().notes:
        duration = note.duration.quarterLength
        pitch = note.pitch if isinstance(note, music21.note.Note) else 'z'  # 'z' for rest
        abc_note = f"{pitch}{duration}"
        notes.append(abc_note)
    
    abc_content = abc_header + ' '.join(notes) + '|'

    with open(abc_file_path, 'w') as abc_file:
        abc_file.write(abc_content)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Convert MIDI to ABC notation')
    parser.add_argument('--midi', '-m', required=True, help='Input .midi file')
    parser.add_argument('output_file', nargs='?', help='Output .abc file (defaults `to output.abc`)', default='output.abc')
    args = parser.parse_args()

    midi_to_abc(args.midi, args.output_file)
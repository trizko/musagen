from music21 import converter

def abc_to_midi(abc_string, output_file):
    # Convert the ABC notation to a music21 stream
    abc_stream = converter.parse(abc_string, format='abc')
    
    # Write the stream to a MIDI file
    midi_path = f"{output_file}.midi"
    abc_stream.write('midi', fp=midi_path)
    
    print(f"MIDI file saved as {midi_path}")

# Example usage
abc_notation = """
X:1
T:Example
M:4/4
K:C
cdef gabc'|
"""

if __name__ == "__main__":
    abc_to_midi(abc_notation, "output")

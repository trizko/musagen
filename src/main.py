from utils import midi_to_wav

import streamlit as st

st.title("Musagen")

midi = st.file_uploader("MIDI file", type=["mid", "midi"], accept_multiple_files=False)
soundfont = st.file_uploader("SoundFont file (optional)", type=["sf2"], accept_multiple_files=False)

if st.button("Generate"):
    if midi is None:
        st.error("Please upload a MIDI file")
    else:
        midi_filename = "input.mid"
        with open(midi_filename, "wb") as f:
            f.write(midi.getbuffer())
        if soundfont is not None:
            soundfont_filename = "soundfont.sf2"
            with open(soundfont_filename, "wb") as f:
                f.write(soundfont.getbuffer())
        else:
            soundfont_filename = ""
        midi_to_wav(midi_filename, soundfont_filename, "output.wav")
        st.audio("output.wav", format="audio/wav")
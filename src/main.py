from basic_pitch.inference import predict
from basic_pitch import ICASSP_2022_MODEL_PATH

import streamlit as st

st.title("Loopy")

midi = st.file_uploader("Audio file", type=["wav"], accept_multiple_files=False)

if st.button("Generate"):
    if midi is None:
        st.error("Please upload a MIDI file")
    else:
        midi_filename = "input.mid"
        with open(midi_filename, "wb") as f:
            f.write(midi.getbuffer())
        model_output, midi_data, note_events = predict(midi_filename, ICASSP_2022_MODEL_PATH)
        st.write(model_output)
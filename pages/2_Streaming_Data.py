import streamlit as st

st.set_page_config(page_title="Stream", page_icon=":studio_microphone:", layout="wide")


title_style = """
            <style>
            .title {
                text-align: center;
                color:#faa356;
            }
            </style>
        """
st.markdown(title_style, unsafe_allow_html=True)

st.markdown("<h1 class='title'>Streaming Data Transcription <span style='color:#b3cee5'>&#x1F50A;</span>&#x23F3;</h1>",
            unsafe_allow_html=True)
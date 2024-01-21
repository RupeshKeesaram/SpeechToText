import streamlit as st
import streamlit_extras.add_vertical_space as avs
from streamlit_extras.switch_page_button import switch_page


# configuring home page
st.set_page_config(page_title="Home", page_icon=":speaking_head_in_silhouette:", layout="wide")
title_style = """
            <style>
            .title {
                text-align: center;
                color:#faa356;
            }
            </style>
        """
st.markdown(title_style, unsafe_allow_html=True)


# Page heading
st.markdown("<h1 class='title'>Speech To Text <span style='color:#b3cee5'>&#x1F50A;</span>&#x1F4DC;</h1>",
            unsafe_allow_html=True)

# sidebar
st.sidebar.success("Select any page above")

# introduction markdown text
intro = """
        <h3 style="color:#a2d2fb">Introduction</h3>

        Automatic Speech Recognition (ASR) is a transformative technology that enables machines to convert spoken language into written text, facilitating seamless interaction between humans and computers.Computer algorithms facilitate this process in four steps: <span style="color:#7ce38b">analyze the audio </span>, <span style="color:#7ce38b"> break it down into parts </span>, <span style="color:#7ce38b"> convert it into a computer-readable format </span>, and <span style="color:#7ce38b"> use the algorithm again to match it into a text-readable format.</span><br>
        
        > <span style="color:#7ce38b">Analyze The Audio </span>:- 
        In the first step of ASR, the audio undergoes detailed analysis, extracting features like frequency patterns and acoustic characteristics. This enables the system to discern speech from background noise and capture nuances in tone and pronunciation.

        > <span style="color:#7ce38b">Break It into Parts</span> :- 
        Following analysis, the ASR system segments the audio, identifying pauses and distinct speech patterns. This step enhances recognition accuracy by breaking the input into manageable linguistic components.

        > <span style="color:#7ce38b">Convert Into Computer Readable Format</span>:- 
        Once segmented, components are transformed into a computer-readable format, often using Mel-frequency cepstral coefficients (MFCCs) or spectrograms. This conversion bridges the gap between raw audio and computational models for advanced analysis.
        
        > <span style="color:#7ce38b">Use Algorithm To Match Text</span>:- 
        Utilizing sophisticated algorithms, ASR matches extracted features to linguistic patterns, generating a word sequence. This final step involves probabilistic decision-making, resulting in the conversion of spoken language into written text for applications like transcription services and voice commands.
        
        """
st.markdown(intro, unsafe_allow_html=True)


# adding vertical spaces
avs.add_vertical_space(2)


# functionalities text
functionality = """
        <h3 style="color:#a2d2fb">Functionalities </h3>

        > The <span style="color:#7ce38b">"Batch Data"</span> page of the Streamlit app offers users a comprehensive solution for audio transcription from pre-recorded files. Users can effortlessly upload audio files in various formats, including MP3 and WAV. The streamlined interface guides users to a "Generate" button, initiating the transcription process. Additionally, a notable feature allows users to visualize audio signals through an "Audio Signals Plot," enabling a before-and-after comparison of audio with and without noise preprocessing. This serves as a valuable tool for assessing the effectiveness of noise reduction techniques. The final transcription is displayed on the page, providing users with accurate and easily accessible text versions of their audio content.
        
        > The <span style="color:#7ce38b">"Streaming Data"</span> page is designed for real-time audio transcription, offering users the ability to capture and transcribe live voice recordings. A user-friendly interface showcases a microphone icon, allowing users to start and stop recording with a simple click. This feature is particularly useful for capturing spontaneous conversations, meetings, or any spoken content as it happens. The system immediately processes the recorded audio, providing users with a real-time transcription on the same page. Additional settings, such as language selection and transcription formatting, enhance the user experience. Users can conveniently save or copy the transcribed content, making this page a versatile tool for on-the-fly audio-to-text conversion.
        """
st.markdown(functionality, unsafe_allow_html=True)

# adding vertical spaces
avs.add_vertical_space(2)


# user guide markdown text
using = """
        <h3 style="color:#a2d2fb">Usage Guide</h3>
        Explore the individual pages below.
        """
st.markdown(using, unsafe_allow_html=True)
avs.add_vertical_space(2)


# main function
def main():
    pages_dict = {
            "home":"home","batch data":"Batch Data Page","steaming data":"Streaming Data Page"
        }
    option = st.selectbox(label="select one page",options=pages_dict.keys())

    if option!="home":
        switch_page(option)


    # # hiding hamburger menu while execution
    # hide_menu_style = """
    #                <style>
    #                #MainMenu {visibility: hidden;}
    #                .stApp [data-testid="stToolbar"]{display:none;}
    #                footer {visibility:hidden}
    #                </style>
    #                """
    # st.markdown(hide_menu_style, unsafe_allow_html=True)


# calling main function
main()
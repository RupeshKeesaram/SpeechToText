import streamlit as st
import assemblyai as aai
from private_keys import ASSEMBLY_AI_KEY
import time
import streamlit_extras.add_vertical_space as avs
from pydub import AudioSegment
import os
from utilities.play_audio import play_wav_file
from utilities.plot_graphs import plot_graph
from utilities.get_transcripts import get_transcripts

# setting api key for assembly ai
aai.settings.api_key = ASSEMBLY_AI_KEY


# main function to display text
def main():
    st.set_page_config(page_title="Batch", page_icon=":file_folder:", layout="wide")

    # text alignment
    title_style = """
            <style>
            .title {
                text-align: center;
                color:#faa356;
            }
            </style>
        """
    st.markdown(title_style, unsafe_allow_html=True)

    # hiding hamburger menu
    hide_menu_style = """
                       <style>
                       #MainMenu {visibility: hidden;}
                       .stApp [data-testid="stToolbar"]{display:none;}
                       footer {visibility:hidden}
                       </style>
                       """
    st.markdown(hide_menu_style, unsafe_allow_html=True)

    # header
    st.markdown("<h1 class='title'>Batch Data Transcription <span style='color:#b3cee5'>&#x1F4BB;</span>&#x1F4D3;</h1>",
                unsafe_allow_html=True)



    # objective markdown text
    objective = """
    <h3 style="color:#a2d2fb">Objective</h3>
    
    > The objective of this page is to empower users to effortlessly transcribe pre-recorded audio files. By providing a seamless and user-friendly interface, this page allows users to upload audio files in various formats and generate accurate text transcriptions with a simple click. Additionally, the inclusion of an "Audio Signals Plot" feature enables users to visually assess the impact of noise preprocessing on their audio data. The page aims to offer a comprehensive solution for batch audio transcription, ensuring efficiency, accuracy, and user satisfaction throughout the process.
    """
    st.markdown(objective, unsafe_allow_html=True)



    # usage markdown text
    using = """
    <h3 style="color:#a2d2fb">How to Use ?</h3>
    
    <span style="color:#7ce38b">1. Upload Audio File:</span>
    Navigate to the "Batch Data" page and locate the "Upload Audio" section. Click on the designated area or button to upload your audio file. Supported formats include MP3, WAV, and more.
    
    <span style="color:#7ce38b">2. Generate Transcription:</span>
    After uploading the audio file, find the "Generate" button and click on it. This initiates the transcription process. Wait for the system to process the audio and generate the text transcription.
    
    <span style="color:#7ce38b">3. Plot Audio Signals:</span>
    Explore the "Audio Signals Plot" feature to visualize the audio data. This comparison graph allows you to analyze the audio signals before and after noise preprocessing. Use it to assess the effectiveness of noise reduction techniques.
    
    <span style="color:#7ce38b">4. Review Transcription:</span>
    Once the transcription is complete, the text result will be displayed on the page. Review the transcription for accuracy. You can copy the text or download it for further use.
    """

    st.markdown(using, unsafe_allow_html=True)


    # file upload header
    file_upload = """
     <h3 style="color:#a2d2fb">Audio Transcriber</h3>
    """
    st.markdown(file_upload, unsafe_allow_html=True)


    # creating columns to take file input & create a visualiza button to visualize the audio
    col1, col2, col3 = st.columns([3, 1, 1])

    transribe_col1, transcribe_col2, transcribe_col3 = st.columns([3, 1, 1])


    # creating file upload input widget
    uploaded_file = ""
    with col1:
        uploaded_file = st.file_uploader("Choose a file", help="Please upload a audio file", type=["m4a", "mp3", "wav"])

        BASE_PATH = "../SpeechToText"
        file_path = ""


        # removing all the files if directory already exits
        for file in os.listdir("data"):
            file_path = os.path.join("data", file)
            os.remove(file_path)

        if uploaded_file:
            # checking the file type & saving on server
            file_name = uploaded_file.name
            if file_name.endswith(".mp3"):
                wav_file = AudioSegment.from_mp3(uploaded_file)
                wav_file.export("data/{}".format(file_name), format=".mp3")
            else:
                wav_file = AudioSegment.from_wav(uploaded_file)
                wav_file.export("data/{}".format(file_name), format="wav")

    # creating "play audio" button
    with col2:
        avs.add_vertical_space(3)
        if uploaded_file:
            audio_file = open(f"data/{file_name}", 'rb')
            audio_bytes = audio_file.read()
            st.audio(audio_bytes, format='audio/ogg')
            # st.audio(file_path,)
        avs.add_vertical_space(3)
        # play_button = st.button(label="Play Audio", type="primary")
        # if play_button:
        #     # throwing an error if file was not uploaded
        #     if not uploaded_file:
        #         error = st.error("Upload an audio file.")
        #         time.sleep(1)
        #         error.empty()
        #     else:
        #         st.audio(file_path)
        #         # calling play_wav_file() to play audio file
        #         with st.spinner("Playing Audio..!!"):
        #             play_wav_file(file_path)


    # creating "transcribe audio" button
    with col3:
        avs.add_vertical_space(3)
        transcribe_btn = st.button("Transcribe Audio", type="primary")
        with st.spinner("Transcribing Audio..!!"):
            if transcribe_btn:
                # throwing an error if file was not uploaded
                if not uploaded_file:
                    error = st.error("Upload an audio file.")
                    time.sleep(1)
                    error.empty()
                else:
                    with transribe_col1:
                        # calling get_transcripts() to get the transcripts
                        if uploaded_file.name.endswith('wav'):
                            transcripts, audio_duration, t_duration = get_transcripts(file_path)
                            st.markdown('<h3 style="color:#a2d2fb">Transcripts</h3>', unsafe_allow_html=True)
                            st.text_area(label=" ", value=transcripts)

                            # markdown text for showing audio file duration / length
                            with transcribe_col2:
                                avs.add_vertical_space(5)
                                st.metric(label="Audio Duration", value=audio_duration)

                            # markdown text for showing time taken to transcribe the audio file
                            with transcribe_col3:
                                avs.add_vertical_space(5)
                                st.metric(label="Time took to transcribe", value=t_duration)

    avs.add_vertical_space(3)

    # markdown text for plotting
    plotting = """
    <h3 style="color:#a2d2fb">Visual Representation of Audio File</h1>
    """
    st.markdown(plotting, unsafe_allow_html=True)


    # creating columns to show visual representation of  audio file
    plt1, plt2 = st.columns(2)

    # creating "Visualize Audio" button
    visualize_button = st.button("Visualize Audio", type="primary")
    if visualize_button:

        # throwing error if file was not uploaded
        if not uploaded_file:
            error = st.error("Please upload a audio file....")
            time.sleep(1)
            error.empty()
        else:
            with plt1:
                # calling plot_graph() to plot the audio file
                with st.spinner("Plotting...!!"):
                    fig = plot_graph(file_path)
                    st.pyplot(fig)



# calling main function
main()

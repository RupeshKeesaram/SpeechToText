import assemblyai as aai
import pandas as pd

aai.settings.api_key = "8abcf02c0ed4499193f9170429741398"


def on_open(session_opened: aai.RealtimeSessionOpened):
    print("Session ID:", session_opened.session_id)


def on_data(transcript: aai.RealtimeTranscript):
    if not transcript.text:
        return

    if isinstance(transcript, aai.RealtimeFinalTranscript):
        print(transcript.text, end="\r\n")
    else:
        print(transcript.text, end="\r")


def on_error(error: aai.RealtimeError):
    print("An error occured:", error)


def on_close():
    print("Closing Session")

def load_data():
    df = pd.read_excel(r"C:\Users\KeesaramRupesh\Downloads\Trading terms1.xlsx")
    words = df["Terms"]
    return list(words)

words  = load_data()

def connect():
    transcriber = aai.RealtimeTranscriber(
    sample_rate=16_000,
    on_data=on_data,
    on_error=on_error,
    on_open=on_open,
    on_close=on_close,
    # word_boost=words
    )

    return transcriber
import assemblyai as aai
import wave
import time


# function to get the transcripts
def get_transcripts(file) -> tuple:
    """
    :param file:
    :return tuple containing transcribed text,audio duration,time took to transcribe:
    """
    # reading .wav file
    file_obj = wave.open(file, "rb")

    # getting frame rate
    fs = file_obj.getframerate()

    # getting nframes
    nframes = file_obj.getnframes()

    # calculating audio length ( in sec )
    t_audio = nframes / fs

    # initializing transcriber object
    transcriber = aai.Transcriber()

    t1 = time.time()

    # calling transcribe API to get the transcripts
    transcripts = transcriber.transcribe(file)
    duration = time.time() - t1

    return transcripts.text, t_audio, duration

import assemblyai as aai
import wave
import time


def get_transcripts(file):
    file_obj = wave.open(file,"rb")
    fs = file_obj.getframerate()
    nframes = file_obj.getnframes()

    t_audio = nframes/fs

    transcriber = aai.Transcriber()

    t1 = time.time()
    transcripts = transcriber.transcribe(file)
    duration = time.time()-t1

    return transcripts.text,t_audio,duration
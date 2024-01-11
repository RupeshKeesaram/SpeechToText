import wave
import pyaudio as pa

def play_wav_file(file):
    file_obj = wave.open(file, "rb")
    chunk = 1024

    p = pa.PyAudio()

    stream = p.open(format=p.get_format_from_width(file_obj.getsampwidth()),
                    channels=file_obj.getnchannels(),
                    rate=file_obj.getframerate(),
                    output=True)

    data = file_obj.readframes(chunk)

    # Play the sound by writing the audio data to the stream
    while data !=b'':
        stream.write(data)
        data = file_obj.readframes(chunk)

    # Close and terminate the stream
    stream.close()
    p.terminate()
    file_obj.close()
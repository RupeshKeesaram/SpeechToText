import wave
import pyaudio as pa


# defining function to play audio file
def play_wav_file(file):
    """

    :param file:
    :return None:
    """

    # reading audio file
    file_obj = wave.open(file, "rb")
    chunk = 1024

    # creating a pyaudio object
    p = pa.PyAudio()

    # print("Available devices:\n")
    # for i in range(0, p.get_device_count()):
    #     info = p.get_device_info_by_index(i)
    #     print(str(info["index"]) + ": \t %s \n \t %s \n" % (
    #     info["name"], p.get_host_api_info_by_index(info["hostApi"])["name"]))
    #     pass

    # creating a output stream
    stream = p.open(format=p.get_format_from_width(file_obj.getsampwidth()),
                    channels=file_obj.getnchannels(),
                    rate=file_obj.getframerate(),
                    output=True)

    # reading data in frames
    data = file_obj.readframes(chunk)

    # Play the sound by writing the audio data to the stream
    while data !=b'':
        stream.write(data)
        data = file_obj.readframes(chunk)

    # Close and terminate the stream
    stream.close()
    p.terminate()
    file_obj.close()
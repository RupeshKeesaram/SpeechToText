import wave
import matplotlib.pyplot as plt
import numpy as np
import pyaudio as pa
import assemblyai as aai

# file= wave.open(r"C:\Users\KeesaramRupesh\OneDrive - Xformics Inc\Documents\Sound Recordings\harvard.wav","rb")
#
# print("No of channels :- ",file.getnchannels())
# print("No of frames per sec  :- ",file.getframerate())
# print("Sample Width :- ",file.getsampwidth())
# print("No of frames :- ",file.getnframes())
# print("Parameters :- ",file.getparams())
#
# audio_duration = file.getnframes()/file.getframerate()
#
# print("Durartion :- ",audio_duration)
#
# frames = file.readframes(-1)
# print(type(frames),type(frames[0]))
# print(len(frames)//4)
#
# file.close()
#
#
# samp_wav = wave.open(r"C:\Users\KeesaramRupesh\OneDrive - Xformics Inc\Documents\Sound Recordings\sampple.wav","wb")
#
# samp_wav.setframerate(44100)
# samp_wav.setnchannels(2)
# samp_wav.setsampwidth(2)
# print(len(frames))
# samp_wav.writeframes(frames[:500000])
# samp_wav.close()



### Plotting Audio File

# file_obj = wave.open(r"C:\Users\KeesaramRupesh\OneDrive - Xformics Inc\Documents\Sound Recordings\harvard.wav","rb")
# nframes = file_obj.getnframes()
# frame_rate = file_obj.getframerate()
# signal_wave = file_obj.readframes(-1)
# file_obj.close()
#
#
# t_audio = nframes/frame_rate
# print(t_audio)
# print(nframes)
#
# signal_array = np.frombuffer(signal_wave,dtype=np.int16)
# t_arry = np.linspace(0,t_audio,num=nframes*2)
#
# plt.figure(figsize=(15,5))
# plt.plot(t_arry,signal_array)
# plt.title("Audio Wave")
# plt.ylabel("Signal wave")
# plt.xlabel("Time (s)")
# plt.xlim(0,t_audio)
# plt.show()



## Recording Audio Using Microphone


CHUNK = 2400
FRAME_RATE = 44100
CHANNELS = 2
sample_format = pa.paInt16
seconds = 5
filename = "sampe_wav.wav"

p = pa.PyAudio()
print("Started Recording!!!")

# creating a stream object

stream = p.open(format=sample_format,channels=CHANNELS,
                frames_per_buffer=CHUNK,rate=FRAME_RATE,input=True)

frames = []
for i in range(0,FRAME_RATE//CHUNK*seconds):
    data = stream.read(CHUNK)
    frames.append(data)


stream.stop_stream()
stream.close()
p.terminate()

print("Finished Recording")


# saving the recorded audio into a .wav file

file_obj = wave.open("sample.wav","wb")
file_obj.setnchannels(2)
file_obj.setframerate(44100)
file_obj.setsampwidth(p.get_sample_size(sample_format))
file_obj.writeframes(b''.join(frames))
file_obj.close()




# API key ( Replace this with yours )
aai.settings.api_key = "99762b9d57be482881cd3e1162f7c070"

FILE_URL = "sample.wav"

# intializing a transcriber
transcriber = aai.Transcriber()
transcript = transcriber.transcribe(FILE_URL)


print(transcript.text)

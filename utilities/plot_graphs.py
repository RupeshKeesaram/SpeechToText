import wave
import matplotlib.pyplot as plt
import numpy as np


def plot_graph(file):
    file_obj = wave.open(file, "rb")
    nframes = file_obj.getnframes()
    frame_rate = file_obj.getframerate()
    signal_wave = file_obj.readframes(-1)
    file_obj.close()

    t_audio = nframes/frame_rate

    signal_array = np.frombuffer(signal_wave,dtype=np.int16)
    t_arry = np.linspace(0,t_audio,num=nframes*2)

    # return signal_array,t_arry
    fig = plt.figure(figsize=(15,5))
    plt.plot(t_arry,signal_array)
    plt.plot(t_arry,signal_array)
    plt.title("Audio Wave")
    plt.ylabel("Signal wave")
    plt.xlabel("Time (s)")
    plt.xlim(0,t_audio)
    return fig
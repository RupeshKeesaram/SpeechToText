import wave
import matplotlib.pyplot as plt
import numpy as np


# defining a function to plot graphs
def plot_graph(file):
    """
        Generates a matplotlib.pyplot figure based on data from the given file.

        :param file: Path to the input file containing data for the plot.
        :type file: str
        :return: A matplotlib.pyplot figure object displaying the desired plot.
        :rtype: matplotlib.figure.Figure
    """

    # reading audio file
    file_obj = wave.open(file, "rb")

    # getting file properties
    nframes = file_obj.getnframes()
    frame_rate = file_obj.getframerate()
    signal_wave = file_obj.readframes(-1)

    # closing file obj
    file_obj.close()

    # audio duration ( in sec )
    t_audio = nframes/frame_rate

    # creating data for x & y axis
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
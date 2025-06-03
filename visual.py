import matplotlib.pyplot as plt 
import scipy.io.wavfile as wavfile
import wave 
import numpy as np 

def visualize_wave(path): 
    #read audio file 
    audio = wave.open(path) 
    #read frames, -1 = all frames
    signal = audio.readframes(-1) 
    signal = np.frombuffer(signal, dytype='int16')
    #frame rate 
    f_rate = audio.getframerate()

    time = np.linspace(0, len(signal)/f_rate, num = len(signal))
    plt.figure(1)
    plt.ylabel('amplitude')
    plt.xlabel('time')
    plt.plot(time, signal)
    plt.show() 

def spectrogram(path): 
    Fs, aud = wavfile.read(path)
    aud = aud[:0] 
    first = aud[:int(Fs*125)] 
    powerSpectrum, frequenciesFound, time, imageAxis = plt.specgram(first, Fs=Fs)
    plt.show()
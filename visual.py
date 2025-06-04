import matplotlib.pyplot as plt 
import wave 
import numpy as np 
import sys
import librosa 

def visualize_wave(path): 
    #read audio file 
    audio = wave.open(path) 
    #read frames, -1 = all frames
    signal = audio.readframes(-1) 
    signal = np.frombuffer(signal, dtype='int16')
    #frame rate 
    f_rate = audio.getframerate()

    time = np.linspace(0, len(signal)/f_rate, num = len(signal))
    plt.figure(1)
    plt.ylabel('amplitude')
    plt.xlabel('time')
    plt.plot(time, signal)
    plt.show() 

def spectrogram(path): 
    aud, sr = librosa.load(path, sr=44100)
    X = librosa.stft(aud)
    Xdb = librosa.amplitude_to_db(abs(X))
    plt.figure(figsize=(14, 5))
    librosa.display.specshow(Xdb, sr=sr, x_axis='time', y_axis='log')
    plt.colorbar()
    plt.show()

if sys.argv[2] == "wave": 
    visualize_wave(sys.argv[1])
if sys.argv[2] == "spectrogram":
    spectrogram(sys.argv[1])


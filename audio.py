import wave 
import shutil 
import matplotlib.pyplot as plt 
import scipy.io.wavfile as wavfile

#path: the audio file name 
def audio_to_bits(path): 
    audio = wave.open(path, mode = 'rb')
    arr = list(audio.readframes(audio.getnframes())) #converts frames into a list
    arr = bytearray(arr) #converts to bytes
    try: 
        with open("temp.txt", "wb") as f: #write to file
            f.write(arr)
    except FileNotFoundError: 
        print("File not found")

    shutil.copy(path, 'modified_audio.wav') #copy audio file into a new file to be modified


#path: the modified audio file name
def bits_to_audio(path): 
    try: 
        with open("encode.txt", "rb") as f: #read bytes from file
            byte_arr = bytearray(f.read())
    except FileNotFoundError: 
        print("File not found")

    with wave.open(path, 'wb') as wav: 
        wav.writeframes(byte_arr)


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


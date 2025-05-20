import wave 

def audio_bits(path): 
    audio = wave.open(path, mode = 'rb')
    arr = list(audio.readframes(audio.getnframes()))
    print(type(arr))

audio_bits('cyber.wav')

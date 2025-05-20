import wave 

def audio_bits(path): 
    audio = wave.open(path, mode = 'rb')
    arr = list(audio.readframes(audio.getnframes())) #converts frames into a list
    arr = bytearray(arr) #converts to bytes
    with open("temp.txt", "wb") as f:
        f.write(arr)
        

audio_bits('cyber.wav')

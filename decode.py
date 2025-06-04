import wave 

#path: the audio file name
#converts the wav file into a byte array 
#returns a byte array 
def audio_to_bits(path): 
    audio = wave.open(path, mode = 'rb')
    arr = list(audio.readframes(audio.getnframes())) #converts frames into a list
    return bytearray(arr)


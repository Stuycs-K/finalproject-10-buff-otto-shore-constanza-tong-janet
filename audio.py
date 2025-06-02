import wave 
import shutil 
import os

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

        


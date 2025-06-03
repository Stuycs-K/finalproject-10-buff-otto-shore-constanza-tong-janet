import wave 
import shutil
import sys

#path: the audio file name
#new_path: the new audio file name
#converts the wav file into a byte array 
def audio_to_bits(path, new_path): 
    shutil.copy(path, new_path)
    audio = wave.open(path, mode = 'rb')
    arr = list(audio.readframes(audio.getnframes())) #converts frames into a list
    arr = bytearray(arr) #converts to bytes

#message: the message to be encoded 
#converts the message to a bit array
def message_to_bits(message): 
    bit_array = [] 
    for char in message: 
        binary = bin(ord(char))[2:] 
        binary = '0' * (8 - len(binary)) + binary #get bit string for each char
        for b in binary: 
            bit_array.append(int(b))
    return bit_array 
        
#message: message in bit array 
#byte_array: the byte array of the audio
#encodes each bit into the lsb of the byte array
def encode(message, byte_array): 
    message += int((len(byte_array) - len(message)*8*8)/8) * '&'
    message_array = message_to_bits(message)
    for i in range(len(byte_array)): 
        byte_array[i] = (byte_array[i] & 254) | message_array[i]
    return bytes(byte_array)

#path: the modified audio file name
#byte_array: the modified bytes
def bits_to_audio(path, byte_array): 
    with wave.open(path, 'wb') as wav: 
        wav.writeframes(byte_array) 



if len(sys.argv) == 2: 
    audio_to_bits('wavFiles/raw/' + sys.argv[1])
else: 
    bits_to_audio('wavFiles/raw/' +sys.argv[1], 'wavFiles/encoded/' + sys.argv[2])



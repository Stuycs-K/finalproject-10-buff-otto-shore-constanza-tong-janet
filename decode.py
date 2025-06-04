import wave 
import sys

#path: the audio file name
#converts the wav file into a byte array 
#returns a byte array 
def audio_to_bits(path): 
    audio = wave.open(path, mode = 'rb')
    arr = list(audio.readframes(audio.getnframes())) #converts frames into a list
    return bytearray(arr)

def decode(byte_array, increment): 
    message_bits = ""
    message = ""
    for i in range(0, len(byte_array), increment): 
        message_bits += str(byte_array[i] & 1)
    for i in range(0, len(message_bits), 8): 
        message += chr(int(message_bits[i:i+8], 2))
    
    return message.split("&&&&")[0]

def decode2(byte_array, increment): 
    message_bits = ""
    message = ""
    for i in range(0, len(byte_array), increment): 
        curr_byte = byte_array[i]
        if (curr_byte & 192) == 192:
            message_bits += str(byte_array[i] & 1)
    for i in range(0, len(message_bits), 8): 
        message += chr(int(message_bits[i:i+8], 2))
    
    return message.split("&&&&")[0]



def main(path, increment): 
    byte_array = audio_to_bits(path) 
    message = decode(byte_array, increment) 
    print(message)
    
def main2(path, increment): 
    byte_array = audio_to_bits(path) 
    message = decode2(byte_array, increment) 
    print(message)

if (len(sys.argv) - 1) == 2:
    if sys.argv[2] == 'msb':
        main2('wavFiles/encoded/' + sys.argv[1], sys.argv[2])
    else:
        main('wavFiles/encoded/' + sys.argv[1], sys.argv[2])
else:
    main('wavFiles/encoded/' + sys.argv[1], 1)

import wave 
import sys

#path: the audio file name
#converts the wav file into a byte array 
#returns a byte array 
def audio_to_bits(path): 
    audio = wave.open(path, mode = 'rb')
    arr = list(audio.readframes(audio.getnframes())) #converts frames into a list
    return bytearray(arr)

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
        
#message: message in string
#byte_array: the byte array of the audio
#encodes each bit into the lsb of the byte array
def encode(message, byte_array):
    message = message + int(len(byte_array)/8 - len(message)) * '&'
    message_array = message_to_bits(message)
    for i in range(len(byte_array)): 
        byte_array[i] = (byte_array[i] & 254) | message_array[i]
    return bytes(byte_array)
    
#NEW
#message: message in string
#byte_array: the byte array of the audio
#increment: how many bytes to skip when encoding
#encodes each bit into the lsb of the byte array, but skip every [increment] number of bytes
def encode2(message, byte_array, increment):
    message = message + int(len(byte_array)/8 - len(message)) * '&'
    message_array = message_to_bits(message)
    for i in range(0, len(byte_array), increment): 
        byte_array[i] = (byte_array[i] & 254) | message_array[int(i/increment)]
    return bytes(byte_array)
  
#NEW  
#message: message in string
#byte_array: the byte array of the audio
#encodes each bit into the lsb of the byte array, but only if the 2 most significant bits are 1
def encode3(message, byte_array):
    message = message + int(len(byte_array)/8 - len(message)) * '&'
    message_array = message_to_bits(message)
    j = 0
    for i in range(len(byte_array)): 
        curr_byte = byte_array[i]
        if (curr_byte & 192) == 192:
            byte_array[i] = (byte_array[i] & 254) | message_array[j]
            j += 1
    return bytes(byte_array)  
   

#path: the modified audio file name
#new_path: the new audio file 
#byte_array: the modified bytes
def bits_to_audio(path, new_path, byte_array): 
    with wave.open(new_path, 'wb') as wav:
        audio = wave.open(path, mode='rb')
        wav.setparams(audio.getparams()) 
        wav.writeframes(byte_array) 
    audio.close()


def main(path, new_path, message): 
    byte_array = audio_to_bits(path)
    new_bytes = encode(message, byte_array)
    bits_to_audio(path, new_path, new_bytes)

# NEW
# to encode every increment bytes
def main2(path, new_path, message, increment): 
    byte_array = audio_to_bits(path)
    new_bytes = encode2(message, byte_array, increment)
    bits_to_audio(path, new_path, new_bytes)
    
# NEW
# to encode only bytes starting with 11
def main3(path, new_path, message): 
    byte_array = audio_to_bits(path)
    new_bytes = encode3(message, byte_array)
    bits_to_audio(path, new_path, new_bytes)


# main('wavFiles/raw/' + sys.argv[1], 'wavFiles/encoded/' + sys.argv[2], sys.argv[3])

#NEW
if (len(sys.argv) - 1) == 4:
    if sys.argv[4] == 'msb':
        main3('wavFiles/raw/' + sys.argv[1], 'wavFiles/encoded/' + sys.argv[2], sys.argv[3])
    else:
        main2('wavFiles/raw/' + sys.argv[1], 'wavFiles/encoded/' + sys.argv[2], sys.argv[3], int(sys.argv[4]))        
else:
    main('wavFiles/raw/' + sys.argv[1], 'wavFiles/encoded/' + sys.argv[2], sys.argv[3])
    
    
     
    




[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/am3xLbu5)
# Audio Steganography
 
### Constanzinnovation et al. 

Otto Buff, Janet Tong, Constanza Shore Coloni
       
### Project Description:

Audio Stegonography (LSB, Spectrograms, etc.)

### Instructions:

##### LSB Audio Steganography 

The user will e able to either encode a message into an audio file or decode an audio file containing a hidden message using makefile targets. 

**ENCODE INSTRUCTIONS**: 
1) Begin by loading the audio of your choice: make loadaudio [INSERT AUDIO FILE]

This audio file must be a wavfile. Find sample wavfiles in the wavFile folder. 

2) Encode your message into the loaded audio: make encode [INSERT MESSAGE]

3) Finally, run the following to insert the modified bytes back into a new wavfile: make returnaudio [INSERT AUDIO FILE] [INSERT NEW AUDIO FILE NAME]

This will create a new encoded wavfile with the user's indicated name. This way, the user can hear faint differences in the audio. 


##### Spectrogram Visualizations

The user will be able to either encode a message into an audio file or decode an audio file containing a hidden message using makefile targets. For encode, the user will have to provide an existing audio file and a text file with the message, and the program will encode the text into the audio. For decode, the user will have to provide an audio file, and the program will search for a message in the LSB and output it into a new text file.

### Resources/ References:
https://www.scielo.org.mx/scielo.php?script=sci_arttext&pid=S1405-55462022000100039 


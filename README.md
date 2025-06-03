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
1) Begin by loading the audio of your choice: make loadaudio ARGS=[INSERT AUDIO FILE NAME]

This audio file must be a wavfile. Find sample raw wavfiles in the wavFiles/raw folder. 

2) Encode your message into the loaded audio: make encode ARGS=[INSERT MESSAGE]

3) Finally, run the following to insert the modified bytes back into a new wavfile: make returnaudio ARGS=[INSERT AUDIO FILE NAME] [INSERT NEW AUDIO FILE NAME]

Ex: make returnaudio ARGS=cyber.wav modified.wav

This will create a new encoded wavfile with the user's indicated name in the wavFiles/encoded folder. This way, the user can hear faint differences in the audio. 

**DECODE INSTRUCTIONS**:
1) The user must again begin by loading the encoded audio file: make loadaudio ARGS=[INSERT AUDIO FILE NAME] 

Find encoded audio files in the encoded folder of wavFiles for testing. 

2) Decode the message: make decode ARGS=[INSERT AUDIO FILE NAME] [INSERT OUTPUT FILE NAME] 

Use the encoded audio file and provide a name for the file with the message. 


##### Spectrogram Visualizations


### Resources/ References:
https://www.scielo.org.mx/scielo.php?script=sci_arttext&pid=S1405-55462022000100039 


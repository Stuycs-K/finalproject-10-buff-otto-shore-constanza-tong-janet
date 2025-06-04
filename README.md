[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/am3xLbu5)
# Audio Steganography
 
### Constanzinnovation et al. 

Otto Buff, Janet Tong, Constanza Shore Coloni
       
### Project Description:

Audio Stegonography (LSB, Spectrograms, etc.)

### Instructions:

##### LSB Audio Steganography 

The user will be able to either encode a message into an audio file or decode an audio file containing a hidden message using makefile targets. 

**ENCODE INSTRUCTIONS**: make encode ARGS=[INSERT AUDIO FILE NAME] [INSERT MODIFIED AUDIO FILE NAME] [THE MESSAGE] 

The first argument is the name of the audio file that the user is encoding the message into: this audio file must be inside the folder wavFiles/raw. The second argument is the name of the modified output audio: when encode is run, the output file can be found inside wavFiles/encoded. The third argument is the message. 

Optionally, the user may include a 4th argument: 
1) They may specify an integer increment n in which the LSB for every nth byte will be changed as opposed to every consecutive byte. 

2) They may alternatively only change the LSB for the "Most Significant Bytes" (a byte is deemed  significant if its first 2 bits are both 1). This feature is toggled by adding the argument "msb" in make encode. 


**DECODE INSTRUCTIONS**: make decode ARGS=[INSERT AUDIO FILE NAME] [INSERT MODIFIED AUDIO FILE NAME] [THE MESSAGE] 



##### Spectrogram Visualizations


### Resources/ References:
https://www.scielo.org.mx/scielo.php?script=sci_arttext&pid=S1405-55462022000100039 


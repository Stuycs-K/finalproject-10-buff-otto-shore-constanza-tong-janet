[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/am3xLbu5)
# Audio Steganography
 
### Constanzinnovation et al. 

Otto Buff, Janet Tong, Constanza Shore Coloni
       
### Project Description:

LSB Audio Stegonography 

### Instructions:

The user will be able to either encode a message into an audio file or decode an audio file containing a hidden message using makefile targets. 

##### **ENCODE INSTRUCTIONS**: make encode ARGS=[INSERT AUDIO FILE NAME] [INSERT MODIFIED AUDIO FILE NAME] [THE MESSAGE] [(optional) MODE] 

The first argument is the name of the audio file that the user is encoding the message into: this audio file must be inside the folder wavFiles/raw. The second argument is the name of the modified output audio: when encode is run, the output file can be found inside wavFiles/encoded. The third argument is the message. 

Optionally, the user may include a 4th argument specifying a mode: 
1) They may specify an integer increment n in which the LSB for every nth byte will be changed as opposed to every consecutive byte. 

2) They may alternatively only change the LSB for the "Most Significant Bytes" (a byte is deemed  significant if its first 2 bits are both 1). This feature is toggled by adding the argument "msb" in make encode. (e.g. make encode ARGS="cyber.wav new_cyber.wav mEsSaGe msb")


##### **DECODE INSTRUCTIONS**: make decode ARGS=[INSERT ENCODED AUDIO FILE NAME] [MODE] 

Note that the audio file must be inside wavFiles/encoded. 

Optionally, the user may include a 2nd argument for the mode, either an increment or specifying that the encoding was "msb". 

##### **VISUAL INSTRUCTIONS** make visual ARGS=[INSERT AUDIO FILE NAME] [MODE(wave or spectrogram)] 

The user first indicates which audio file they want to visualize. There are two modes: wave and spectrogram. The wave mode will produce a graph that maps the amplitude vs time for the audio. The spectrogram mode will produce a spectrogram of the audio that allows the user to observe the changes in frequency through variation in colors. These visuals can help us view encoded files. 

### Resources/ References:
https://www.scielo.org.mx/scielo.php?script=sci_arttext&pid=S1405-55462022000100039 


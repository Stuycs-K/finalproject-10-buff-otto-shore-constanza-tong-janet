[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/am3xLbu5)
# Audio Steganography
 
### Constanzinnovation et al. 

Otto Buff, Janet Tong, Constanza Shore Coloni

### Presentation Materials: 
[Presentation Video](https://drive.google.com/file/d/1fQ4KnOQ__nJ7o4DEzlUVL4eLgY3gRWsB/view?usp=sharing)
[Presentation.md File](https://github.com/Stuycs-K/finalproject-10-buff-otto-shore-constanza-tong-janet/blob/main/Presentation.md)
       
### Project Description:

Our project is LSB Audio Stegonography, where the least significant bits of the bytes of an audio file are changed. This is similar to image stegonography but displays itself differently through nuanced changes in sound. Because LSB Audio Stegonography can be easily cracked, we have added various alterations that make it more secure, including byte increments and only changing bytes that produce louder sounds. 

### Instructions:

**Important:** To run this program, the following python libraries need to be installed: wave, librosa, matplotlib.pyplot, sys, and numpy. 

The user will be able to either encode a message into an audio file or decode an audio file containing a hidden message using makefile targets. 

#### **ENCODE INSTRUCTIONS**: make encode ARGS=[INSERT AUDIO FILE NAME] [INSERT MODIFIED AUDIO FILE NAME] [THE MESSAGE] [(optional) MODE] 

The first argument is the name of the audio file that the user is encoding the message into: this audio file must be inside the folder wavFiles/raw. The second argument is the name of the modified output audio: when encode is run, the output file can be found inside wavFiles/encoded. The third argument is the message. 

Optionally, the user may include a 4th argument specifying a mode: 
1) They may specify an integer increment n in which the LSB for every nth byte will be changed as opposed to every consecutive byte. 

2) They may alternatively only change the LSB for the "Most Significant Bytes" (a byte is deemed  significant if its first 2 bits are both 1). This feature is toggled by adding the argument "msb" in make encode. (e.g. make encode ARGS="cyber.wav new_cyber.wav mEsSaGe msb")


#### **DECODE INSTRUCTIONS**: make decode ARGS=[INSERT ENCODED AUDIO FILE NAME] [(optional) MODE] 

Note that the audio file must be inside wavFiles/encoded. 

Optionally, the user may include a 2nd argument for the mode, either an increment or specifying that the encoding was "msb". 

#### **VISUAL INSTRUCTIONS** make visual ARGS=[INSERT AUDIO FILE NAME] [MODE(wave or spectrogram)] 

The user first indicates which audio file they want to visualize. There are two modes: wave and spectrogram. The wave mode will produce a graph that maps the amplitude vs time for the audio. The spectrogram mode will produce a spectrogram of the audio that allows the user to observe the changes in frequency through variation in colors. These visuals can help us view encoded files. 

Note that for these make commands, the full path is required. For example: make visual ARGS="wavFiles/raw/cyber.wav spectrogram" 

### Resources/ References:
- https://www.scielo.org.mx/scielo.php?script=sci_arttext&pid=S1405-55462022000100039 
    - Overview of LSB steganography
- https://sumit-arora.medium.com/audio-steganography-the-art-of-hiding-secrets-within-earshot-part-2-of-2-c76b1be719b3
    - Used sample code as basis for python encode and decode 
    - Was able to understand LSB concepts from this article 
		- great visuals of LSB, used image in presentation
- https://medium.com/@bikashojha904/from-sound-waves-to-spectrograms-a-comprehensive-guide-to-preparing-audio-datasets-for-asr-1-fa324452f523
    - Used to understand how to render audio waves and how they can be shifted 
- https://medium.com/@AungKyawZall/audio-steganography-39f9fb6d9330
    - Used to explore how software like Coagula and Audacity can be used to hide images within spectrograms of audio 
- https://www.youtube.com/watch?v=1EqCQrVEEVs&ab_channel=ChristianEspinosa 
    - Great visualization for how audacity and paint tools are used to produce audio based on a spectrogram formed from words 
    - Gave inspiration for overlaying images on spectrograms (was unsuccessful in figuring out how to implement however)
- https://manual.audacityteam.org/man/spectrogram_view.html
    - Used manual for spectrograms to understand how to encode information within the graphs (still unsuccessful)
- https://khareanu1612.medium.com/audio-signal-processing-with-spectrograms-and-librosa-b66a0a6bc5cc  
    - Used sample code from librosa library to form spectrograms 
- https://svenruppert.com/2024/04/17/audio-steganography-in-more-detail/
	- Great breakdown of the different methods of audio steganography and their advantages, challenges, and considerations




# Audio Steganography

Audio Steganography: act of hiding secret messages in audio files

### Least Significant Bit (LSB) Insertion

* data is extracted from the audio file, and the bits of the message are hidden in the least significant bits of the audio file
* to extract the message, the least significant bits are extracted and the message is reconstructed

![Alt text](./LSBvisual.png "LSB visual")

* Pros: One of the simplest methods to hide message, and LSB doesn't change the byte by much so it shouldn't be perceptible
* Cons: In an audio file, changing the LSB of every byte might generate noise that has a chance of being noticed by the human

### Modifications

* Instead of changing the LSB of every byte, change it of every other byte or every two or three bytes
* Come up with a way of determining which bytes will get changed, for example if the byte's first two bits are 11

There are also other methods to hide a message, such as phase coding and spread spectrum

### Visual
* spectograms!


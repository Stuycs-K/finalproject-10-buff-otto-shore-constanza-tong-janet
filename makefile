.PHONY: all clear encode decode

all: encode decode

loadaudio: audio.py
	python audio.py $(ARGS)

returnaudio: audio.py 
	python audio.py $(ARGS)
	rm temp.txt

encode: encode.class 
	java Encode temp.txt $(ARGS)

encode.class: encode.java
	javac encode.java

decode: decode.class
	java Decode $(ARGS)

decode.class: decode.java
	javac decode.java

clear:
	rm -f *.class

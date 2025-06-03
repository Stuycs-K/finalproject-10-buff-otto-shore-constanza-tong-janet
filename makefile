.PHONY: all clear encode decode

all: encode decode

loadaudio: audio.py
	python audio.py $(ARGS)

returnaudio: audio.py 
	python audio.py $(ARGS)
	rm temp.txt
	rm encode.txt

encode: encode.class 
	java encode temp.txt $(ARGS)

encode.class: encode.java
	javac encode.java

decode: decode.class
	java decode $(ARGS)

decode.class: decode.java
	javac decode.java

clear:
	rm -f *.class

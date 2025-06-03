.PHONY: all clear encode decode

all: encode decode

encode: encode.class
	java Encode $(ARGS)

encode.class: encode.java
	javac encode.java

decode: decode.class
	java Decode $(ARGS)

decode.class: decode.java
	javac decode.java

clear:
	rm -f *.class

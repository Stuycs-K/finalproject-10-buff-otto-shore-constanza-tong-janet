.PHONY: all encode decode

all: encode decode

encode: encode.py
	python encode.py $(ARGS)

decode: decode.py
	python decode.py $(ARGS)

visual: visual.py 
	python visual.py $(ARGS)


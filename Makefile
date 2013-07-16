#!/usr/bin/make  -f

all: imgkap
	for i in configs/*; do ./oseam2kap $$i; done

clean:  cleandata

cleandata:
	rm -f tmp/*

cleanmaps: cleandata
	rm -f *.kap

cleanall: cleanmaps
	rm -f imgkap imgkap.c

setup: imgkap cleanosr osr osr/composite cleandata
	mkdir tmp
	 
imgkap: imgkap.c
	patch <imgkap.patch
	gcc imgkap.c -lfreeimage -o imgkap
    
imgkap.c:
	wget http://www.dacust.com/inlandwaters/imgkap/v00.01.11/imgkap.c

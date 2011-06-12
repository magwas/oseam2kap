#!/usr/bin/make  -f

all:

clean:  cleandata

cleanosr:
	rm -rf osr

cleandownloaded: cleanosr
	rm -rf osmarender renderer imgkap.c imgkap

cleandata:
	rm -f tmp/*

cleanmaps: cleandata
	rm -f *.kap

cleanall: cleandownloaded cleandata cleanmaps

osmarender:
	svn co http://svn.openstreetmap.org/applications/rendering/osmarender/

renderer:
	svn co http://openseamap.svn.sourceforge.net/svnroot/openseamap/renderer

osr/composite: osr
	./mkcomposites

cleantmp:
	rm -rf tmp

osr: cleanosr
	cp -r osmarender osr
	cp -r renderer/* osr
	cp -r renderer/SeaMapStyles/* osr/stylesheets
	cp -r renderer/SeaMapSymbols/* osr/stylesheets/symbols

setup: imgkap osmarender renderer cleanosr osr osr/composite cleantmp
	mkdir tmp
	 

imgkap: imgkap.c
	gcc imgkap.c -lfreeimage -o imgkap
    
imgkap.c:
	wget http://www.dacust.com/inlandwaters/imgkap/v00.01.11/imgkap.c

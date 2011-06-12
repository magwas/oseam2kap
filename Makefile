#!/usr/bin/make  -f

all:

clean:  cleandata

cleandownloaded:
	rm -rf osmarender renderer

cleandata:
	rm -f tmp/*

cleanmaps: cleandata
	rm -f *.kap

cleanall: cleandownloaded cleandata cleanmaps

setup: cleandownloaded
	svn co http://svn.openstreetmap.org/applications/rendering/osmarender/
	svn co http://openseamap.svn.sourceforge.net/svnroot/openseamap/renderer
	cp -r osmarender osr
	cp -r renderer/* osr
	

#!/usr/bin/python
# coding=UTF-8


d0=-4.85
d0name="%u° %u'"%(int(d0),abs((d0-int(d0))*60))
increase=-8;
print """<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"
xmlns:inkscape="http://www.inkscape.org/namespaces/inkscape"
width="1000" height="1000">
<defs>
    <style xmlns="http://www.w3.org/2000/svg" id="styles" type="text/css">
        .line {
            fill:none;
            stroke:#e50083;
        }
    </style>
</defs>
<rect height="1000" width="1000" fill="#ffffff"/>
<path d="m 480,500 40,0" class="line"/>
<path d="m 500,480 0,40" class="line"/>


"""


print """<path d="m 500,55 0,50" class="line"/>"""
print """<path d="m 500,895 0,50" class="line"/>"""
print """<path d="m 55,500 50,0" class="line"/>"""
print """<path d="m 895,500 50,0" class="line"/>"""
print """<path d="m 500,10 -8.78125,20.90625 -22.625,1.71875 17.15625,14.84375 -5.375,22.03125 19.40625,-11.75 19.3125,11.90625 -5.15625,-22.0625 17.281254,-14.6875 -22.593754,-1.90625 -8.625,-21 z m -0.125,3.5625 0,25.96875 -6.0625,-6.90625 6.0625,-19.0625 z m 27.5625,20.5 -24.6875,8.03125 4.6875,-7.90625 20,-0.125 z m -54.53125,0.125 24.6875,8.03125 -8.4375,3.625 -16.25,-11.65625 z m 25.75,10.875 0.84375,9.15625 -16.09375,11.84375 15.25,-21 z m 3.6875,0 8.9375,2.03125 6.3125,19 -15.25,-21.03125 z"
     id="path8263"
     style="font-size:18px;font-style:normal;font-variant:normal;font-weight:normal;font-stretch:semi-condensed;text-align:center;line-height:125%;text-anchor:middle;fill:#e50083;fill-opacity:1;stroke:none;font-family:DejaVu Sans;-inkscape-font-specification:DejaVu Sans Semi-Condensed"
     inkscape:connector-curvature="0" />
"""

for i in range(360):
    if 0 == (i%10):
        print """<path d="m 500,150 0,20" transform="rotate(%u,500,500)" class="line"/>\n"""%i
        print """<text x="500" y="130" text-anchor="middle"  transform="rotate(%u,500,500)" class="line">%u</text>\n"""%(i,i)
    elif 0 == (i%5):
        print """<path d="m 500,155 0,15" transform="rotate(%u,500,500)" class="line"/>\n"""%i
    else:
        print """<path d="m 500,160 0,10" transform="rotate(%u,500,500)" class="line"/>\n"""%i

print """
<g transform="rotate(%f,500,500)">
    <path d="m 500,180 0,30" class="line"/>
    <path d="m 500,180 5,10" class="line"/>
    <path d="m 500,180 -5,10" class="line"/>
    <path d="m 180,500 30,0" class="line"/>
    <path d="m 500,790 0,30" class="line"/>
    <path d="m 790,500 30,0" class="line"/>
    <path d="m 500,315 0,60" class="line"/>
    <text x="500" y="315" text-anchor="middle" class="line">MAGNETIC</text>
    <path style="fill:none;stroke:none;" inkscape:connector-curvature="0" d="m 400,500 c -1.67204,-109.3864 203.31986,-106.6335 201.64782,0" class="line" id="mycirc" transform="matrix(1,0,0,1.2415823,0,-121.06237)"/>

    <path style="fill:none;stroke:none;" inkscape:connector-curvature="0" d="m 400,500 c -1.67204,109.3864 203.31986,106.6335 201.64782,0" class="line" id="mycircdown" transform="matrix(1,0,0,1.2415823,0,-121.06237)"/>
    <text class="line" text-anchor="middle">
        <textPath xlink:href="#mycirc" startOffset="157"> VAR %s</textPath>
        <textPath xlink:href="#mycircdown" startOffset="157"> ANNUAL INCREASE %s</textPath>
    </text>
"""%(d0,d0name,increase)
for i in range(360):
    if 0 == (i%10):
        print """<path d="m 500,250 0,20" transform="rotate(%f,500,500)" class="line"/>\n"""%(i)
        if 0 == (i%30):
            print """<text x="500" y="230" text-anchor="middle"  transform="rotate(%f,500,500)" class="line">%u</text>\n"""%(i,i)
    elif 0 == (i%5):
        print """<path d="m 500,255 0,15" transform="rotate(%f,500,500)" class="line"/>\n"""%(i)
    else:
        print """<path d="m 500,260 0,10" transform="rotate(%f,500,500)" class="line"/>\n"""%(i)

fq=2.8125
for i in range(128):
    if (0 == (i%32)) and i:
        print """<path d="m 500,275 0,100" transform="rotate(%f,500,500)" class="line"/>\n"""%(i*2.8125) 
    elif 0 == (i%4):
        print """<path d="m 500,275 0,20" transform="rotate(%f,500,500)" class="line"/>\n"""%(i*2.8125) 
    elif 0 == (i%2):
        print """<path d="m 500,275 0,15" transform="rotate(%f,500,500)" class="line"/>\n"""%(i*2.8125) 
    else:
        print """<path d="m 500,275 0,10" transform="rotate(%f,500,500)" class="line"/>\n"""%(i*2.8125) 
print "</g>"


print "</svg>"


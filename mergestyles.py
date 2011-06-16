#!/usr/bin/python

from xml.dom.minidom import parse
import sys

dom1=parse(sys.argv[1])
dom2=parse(sys.argv[2])

s1=dom1.getElementsByTagName("style")[0]
s2=dom2.getElementsByTagName("style")[0]
for n in s2.childNodes:
    s1.appendChild(n.cloneNode(1))

bgstyle = dom1.createTextNode("""
.map-background {
 fill: #f8f8f8;
 stroke: none;
}
""")

s1.appendChild(bgstyle)


s2.parentNode.removeChild(s2)

rules1=dom1.getElementsByTagName("rules")[0]
rules2=dom2.getElementsByTagName("rules")[0]
for n in rules2.childNodes:
    rules1.appendChild(n.cloneNode(1))


rules1.setAttribute("showGrid","yes")
rules1.setAttribute("showLicense","no") #FIXME license moves the chart.

print dom1.toprettyxml()


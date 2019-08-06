"""
Reads in a tex file with bibitems. Prints out a ordered list of bibitems
according to their occurence in the tex file.
"""

import sys
import re

if len(sys.argv) < 2:
    print "Usage: python ordercitations.py filename.tex"
else:
  file = sys.argv[1]

cites = []
count = {}
emptyCount = 0
for line in open(file,"r"):
    for m in re.findall( 'cite{(.*?)\}', line ):
        for cite in  m.split(","):
            temp = cite.strip(' \t\n\r');
            if not temp:
                emptyCount +=1;
                continue
            if not temp in cites:
                cites.append(temp)
                count[temp] = 1
            else:
                count[temp] += 1

for c in cites:
    print("%s %d" % (c, count[c]))

CRED = '\033[91m'
CEND = '\033[0m'
if emptyCount:
    print (CRED + "warning: " + str(emptyCount) + " empty cite{}" + CEND)

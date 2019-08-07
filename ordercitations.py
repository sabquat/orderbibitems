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
  
started = False
items = {}
for line in open(file,"r"):
    if line.startswith('\\end{thebibliography}'):
        started = False
    if started:
        if line.startswith('\\bibitem'):
            name = re.findall( 'bibitem{(.*?)\}', line )[0].strip(' \t\n\r')
            items[name] = line.strip('\n\r')

    if not started and line.startswith('\\begin{thebibliography}'):
        started = True

cites = []
count = {}
emptyCount = 0
for line in open(file,"r"):
    if line[0] == '%':
        continue
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

for c in cites:
    if c in items:
        del items[c]
    else:
        print (CRED + "warning: " + c + " is cited but not listed in bibliography" + CEND)
	
for item in items:
	print (CRED + "warning: " + items[item] + " is unused" + CEND) 

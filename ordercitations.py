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
            items[name] = line
            print name

    if not started and line.startswith('\\begin{thebibliography}'):
        started = True

cites = []
for line in open(file,"r"):
    for m in re.findall( 'cite{(.*?)\}', line ):
        for cite in  m.split(","):

            if not cite.strip(' \t\n\r') in cites:
                cites.append(cite.strip(' \t\n\r'))

for c in cites:
    print items[c]


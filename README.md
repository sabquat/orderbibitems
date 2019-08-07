Order Bibitems
=============

Usage: python ordercitations.py filename.tex

Takes a tex file (with bibitems) as input and returns a list of bibitems according to the occurrence of \cite elements.

It also provides warning if there is any empty \cite{} command or any floating bibitem (i.e., included in reference but not used in the article) or any citation that is not listed on bibliography.

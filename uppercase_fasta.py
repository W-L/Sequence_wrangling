#!/usr/bin/env python3

# transforms all sequences in a fasta to uppercase

import sys

def uppercase_fasta(fa):
    f = open(fa, 'r')
    fu = open(fa + ".upper", 'w+')
    
    for line in f:
        if line[0] == ">":
            fu.write(line)
        else:
            fu.write(line.upper())
            
    f.close()
    fu.close()

for i in sys.argv[1:]:
    uppercase_fasta(i)

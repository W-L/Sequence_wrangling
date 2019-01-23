#! /usr/bin/env python3

import sys

def clean_header(fa):
    f = open(fa, 'r')
    fu = open(fa + ".clean", 'w+')
    
    for line in f:
        if line[0] == ">":
            seq = f.readline()
            if len(seq) > 1000:
                fu.write(line.split('\t')[0] + '\n')
                fu.write(seq)
            else:
                pass
            
        else:
            raise ValueError("weird line:" + str(line))
            
            
    f.close()
    fu.close()

for i in sys.argv[1:]:
    clean_header(i)
    

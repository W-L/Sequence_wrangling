#!/usr/bin/env python3

# chops every sequence in a fasta file into new sequences of a specified length

import sys

fa = sys.argv[1]
n = int(sys.argv[2])

f = open(fa, 'r')
fu_name = fa + ".chopped_" + str(n)
fu = open(fu_name, 'w+')


for line in f:
    if line[0] == ">":
        header = line.rstrip('\n')
        continue
    else:
        line_chunks = [line[i:i+n] for i in range(0, len(line), n)]
        c = 0
        for j in line_chunks:
            j = j.rstrip('\n')
            if len(j) < 10:
                continue
            fu.write(header + ' ' + str(c) + '\n')
            fu.write(str(j) + '\n')
            c += 1
            
fu.close()
f.close()


    
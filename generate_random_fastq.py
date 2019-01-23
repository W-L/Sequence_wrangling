#!/usr/bin/env python3

import random
import sys
import string

read_num = int(sys.argv[1])
read_len = int(sys.argv[2])

sym = list(string.hexdigits)
nuc = ['A','C','G','T']
qual = ['A','B','C','D','E','F','G','H','I']

for i in range(1, read_num + 1):
    h = ''.join(random.choices(sym, k=30))
    head = '@' + h
    comm = '+' + h
    seq = ''.join(random.choices(nuc, k=read_len))
    q = ''.join(random.choices(qual, k=read_len))
    
    print(head)
    print(seq)
    print(comm)
    print(q)




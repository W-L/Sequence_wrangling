#!/usr/bin/env python3
import sys

# chops every sequence in a fastq file into new sequences of a specified length

class Fastq:
    def __init__(self, header, comment, seq, qual):
        self.header = header
        self.comment = comment
        self.sequence = seq
        self.quality = qual


fq = sys.argv[1]
n = int(sys.argv[2])

f = open(fq, 'r')
fu_name = fq + ".chopped_" + str(sys.argv[2])
fu = open(fu_name, 'w+')

seqs = []

for line in f:
    if line[0] == "@":
        header = line.rstrip('\n')
        seq = next(f).rstrip('\n')
        comment = next(f).rstrip('\n')
        qual = next(f).rstrip('\n')

        seqs.append(Fastq(header=header, seq=seq, comment=comment, qual=qual))
    else:
        raise ValueError("line does not start with @")


for read in seqs:
    fu.write(read.header + '\n')
    fu.write(read.sequence[:n] + '\n')
    fu.write(read.comment + '\n')
    fu.write(read.quality[:n] + '\n')

fu.close()
f.close()
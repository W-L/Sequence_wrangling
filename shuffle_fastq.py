#!/usr/bin/env python3
import sys
from random import shuffle

# shuffle a fastq file randomly

class Fastq:
    def __init__(self, header, comment, seq, qual):
        self.header = header
        self.comment = comment
        self.sequence = seq
        self.quality = qual

def read_fastq(filepath):
    seqs = []

    with open(filepath, 'r') as f:
        for line in f:
            if line[0] == "@":
                header = line.rstrip('\n')
                seq = next(f).rstrip('\n')
                comment = next(f).rstrip('\n')
                qual = next(f).rstrip('\n')

                seqs.append(Fastq(header=header, seq=seq, comment=comment, qual=qual))
            else:
                raise ValueError("line does not start with @")

            # DBG
            # if len(seqs) > 10:
            #     break

    return seqs




# input file name
fq = sys.argv[1]
# read the input into memory
seqs = read_fastq(filepath=fq)
# suffle the input sequences
shuffle(seqs)

# write the shuffled sequences
for read in seqs:
    print(read.header)
    print(read.sequence)
    print(read.comment)
    print(read.quality)


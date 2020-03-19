#! /usr/local/bin/python3

# takes an unwrapped fasta file and writes each sequence into a separate file
# args: input output_prefix

import sys


class Fasta:
    def __init__(self, header, seq):
        self.header = header
        self.sequence = seq

def read_fasta(filepath):
    seqs = []

    with open(filepath, 'r') as f:
        for line in f:
            if line[0] == ">":
                header = line.rstrip('\n')
                seq = next(f).rstrip('\n')

                seqs.append(Fasta(header=header, seq=seq))
            else:
                raise ValueError("line does not start with >")

    return seqs


def write_fasta(seqs):
    for i in range(len(seqs)):
        filename = str(sys.argv[2]) + str(i + 1) + '.fa'
        with open(filename, 'w') as fh:
            fh.write(seqs[i].header + '\n')
            fh.write(seqs[i].sequence + '\n')


# runtime
            
file = sys.argv[1]

seqs = read_fasta(file)
write_fasta(seqs)


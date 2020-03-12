#!/usr/bin/env python3
import sys

# split a fastq file into batches of n reads

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

    return seqs

fq = sys.argv[1]
fq_out_base = fq.split('/')[-1].split('.')[0]
seqs = read_fastq(filepath=fq)
n = int(sys.argv[2])
i = n + 1
batch = 0

for read in seqs:
    if i > n:
        fout_name = fq_out_base + '_' + str(n) + '_' + str(batch) + '.fastq'
        i = 1
        batch += 1

    with open(fout_name, 'a') as f:
        f.write(read.header + '\n')
        f.write(read.sequence + '\n')
        f.write(read.comment + '\n')
        f.write(read.quality + '\n')
    i += 1






fu.close()

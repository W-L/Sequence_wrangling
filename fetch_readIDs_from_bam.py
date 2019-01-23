#! /usr/bin/env python3

import sys
import pysam


class Bam:
    
    def __init__(self, filename):
        self.bamfile = pysam.AlignmentFile(filename, 'rb')
        
    def fetch_read_ids(self, fam):
        read_ids = list()
        
        for read in self.bamfile.fetch():
            if read.reference_name == fam:
                read_ids.append(read.query_name)
                
        self.bamfile.close()
        return(read_ids)


class Fastq:
    
    def __init__(self, filename):
        self.name = filename

    def grab_reads(self, id_list):
        c = 0
        
        with open(self.name) as f:
            for r in f:
                rl = r.rstrip('\n').split(' ')
                if rl[0][0] == '@':
                    qname = rl[0].split('@')[1]
                    if qname in id_list:
                        c += 1
                        print(r + f.readline() + f.readline() + f.readline().rstrip('\n'))
                        print(c, file=sys.stderr)

        return(c)
            

bam = Bam(filename=sys.argv[2])
fastq = Fastq(filename=sys.argv[3])

rids = bam.fetch_read_ids(fam=sys.argv[1])
reads = fastq.grab_reads(id_list=rids)

print('DONE', file=sys.stderr)
print(len(rids), file=sys.stderr)
print(reads, file=sys.stderr)


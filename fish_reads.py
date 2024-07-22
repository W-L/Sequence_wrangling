import sys

import mappy


def fetch_rids_of_ref(paf: str, ref: str) -> set:
    rids = set()
    with open(paf, 'r') as paff:
        for line in paff:
            ll = line.split('\t')
            tname = ll[5]
            if tname == ref:
                qname = ll[0]
                rids.add(qname)
    return rids



def fish_reads(fq, rids):
    written = set()
    for name, seq, qual in mappy.fastx_read(fq):
        if name in rids and name not in written:
            print(f'@{name}\n{seq}\n+\n{qual}')
            written.add(name)



if __name__ == '__main__':
    paf_file = sys.argv[1]
    fq_file = sys.argv[2]
    refname = sys.argv[3]

    read_ids = fetch_rids_of_ref(paf_file, refname)
    fish_reads(fq_file, read_ids)




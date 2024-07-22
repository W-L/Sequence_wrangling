import sys
import mappy


def print_fasta_lengths(fasta_file):
    for name, seq, *_ in mappy.fastx_read(fasta_file):
        print(name, len(seq))



if __name__ == '__main__':
    print_fasta_lengths(str(sys.argv[1]))




import sys
import mappy

"""
filter fasta sequences by a given length

python filter_fasta_len.py input min_len 
"""


def process_fasta(fasta_file: str, minimum_len: int) -> None:
    for name, seq, qual in mappy.fastx_read(fasta_file):
        if len(seq) < minimum_len:
            continue
        print(f'>{name}')
        print(seq)


def main() -> None:
    file = sys.argv[1]
    min_len = int(sys.argv[2])
    process_fasta(file, min_len)


if __name__ == '__main__':
    main()

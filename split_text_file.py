import sys
from pathlib import Path
import gzip


def split_text_file(fp: str, lines_per_file: int) -> None:
    # if dealing with fastq, lines_per_file needs to be divisible by 4
    in_suff = Path(fp).suffixes
    if '.fastq' in in_suff or '.fq' in in_suff:
        if lines_per_file % 4 != 0:
            raise ValueError('lines_per_file must be multiple of 4')
    # counter for files
    batch = 0
    # counter for lines
    counter = 0
    # open a new file as the current one to write to
    fpp = Path(fp)
    current_batch = open(f'{fpp.stem}.{batch:03}{"".join(in_suff)}', 'w')
    # loop through the input file
    if Path(fp).suffix == '.gz':
        input_file = gzip.open(fp, 'rt')
    else:
        input_file = open(fp, 'r')

    for line in input_file:
        current_batch.write(line)
        counter += 1
        # once the current file is full, close and open a new one
        if counter % lines_per_file == 0:
            current_batch.close()
            batch += 1
            current_batch = open(f'{fpp.stem}.{batch:03}{"".join(in_suff)}', 'w')
    # close the files
    input_file.close()
    current_batch.close()



if __name__ == '__main__':
    split_text_file(fp=sys.argv[1], lines_per_file=int(sys.argv[2]))



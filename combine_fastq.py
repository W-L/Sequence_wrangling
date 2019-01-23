#! /bin/python3
# combines fasta and qual files from separate files into fastq


import os.path
from glob import glob


def qual_sym(n):
    # takes a quality number
    # and returns the corresponding symbol
    sym = chr(int(n) + 33)
    return sym


def unwrap_fasta(fa):
    f = open(fa, 'r')
    fu_name = fa + ".unwrapped"
    fu = open(fu_name, 'w+')
    seq = ''

    for line in f:
        # when line is a header, write last seq and new header
        if line[0] == ">":
            if len(seq) is not 0:
                seq = seq.replace('\n', '') + '\n'
                fu.write(seq)
            seq = ''
            fu.write(line)
        else:
            seq = seq + line

    # capture last seq when no more headers in file
    seq = seq.replace('\n', '') + '\n'
    fu.write(seq)

    f.close()
    fu.close()
    return


def unwrap_qual(qual_file):
    q = open(qual_file, 'r')
    qu_name = qual_file + ".unwrapped"
    qu = open(qu_name, 'w+')
    seq = ''

    for line in q:
        # when line is a header, write last seq and new header
        if line[0] == ">":
            if len(seq) is not 0:
                seq = seq.replace('\n', '') + '\n'
                qu.write(seq)
            seq = ''
            qu.write(line)
        else:
            line_mod = line.lstrip().rstrip()
            seq = seq + line_mod + ' '

    # capture last seq when no more headers in file
    seq = seq.replace('\n', '') + '\n'
    qu.write(seq)

    q.close()
    qu.close()
    return


def fq(fa, qa):
    # takes a fa file and a quality file and combines them to a fastq
    f = open(fa, 'r')
    q = open(qa, 'r')
    fq_name = fa + ".fastq"
    print(fq_name)
    fq_file = open(fq_name, 'w+')

    for line1, line2 in zip(f, q):
        # no need to read into memory

        if line1 == line2:
            # if the headers of both files are equal then write it
            header = line1.replace(">", "@")
            plus = line1.replace(">", "+")
            fq_file.write(header)

        else:
            # write sequence and get quality symbols
            fq_file.write(line1)
            qual_string = ''
            for n in line2.split():
                qual_string = qual_string + qual_sym(n)

            qual_string = qual_string + '\n'
            fq_file.write(plus)
            fq_file.write(qual_string)

            # test length of seq and quality string
            seq_len = len(line1)
            q_len = len(qual_string)
            if seq_len != q_len:
                print("diff seq len + q len")

    f.close()
    q.close()
    fq_file.close()
    return


def concat(fa_list, name):
    # take all fastq files and concatenate them
    master = open(name, 'w+')
    for element in fa_list:
        f = open(element, 'r')
        for line in f:
            master.write(line)
        f.close()
    master.close()
    return


# --- # --- #


dirs = glob("./d*")

for species in dirs:
    # list of unzipped fasta and qual files
    fasta_list = glob(species + "/fasta.*.fa")
    qual_list = glob(species + "/qual.*.fa")

    # unwrap all the files
    for fasta in fasta_list:
        if os.path.isfile(fasta + ".unwrapped") is False:
            unwrap_fasta(fasta)

    for qual in qual_list:
        if os.path.isfile(qual + ".unwrapped") is False:
            unwrap_qual(qual)

    # redefining lists with unwrapped files
    fasta_list_new = glob(species + "/fasta.*.unwrapped")
    qual_list_new = glob(species + "/qual.*.unwrapped")

    # combine corresponding fasta and qual files into pairs
    pairs = set(zip(fasta_list_new, qual_list_new))

    # create fastq files form pairs
    for pair in pairs:
        if os.path.isfile(pair[0] + ".fastq") is False:
            fq(pair[0], pair[1])

    # concatenate all fastq per species
    fastq_list = glob(species + "/*.fastq")
    fastq_name = "./fastq_files/" + species.split("/")[1] + ".fastq"

    if os.path.isfile(fastq_name) is False:
        concat(fastq_list, fastq_name)

    print(species + " done")

print("done")

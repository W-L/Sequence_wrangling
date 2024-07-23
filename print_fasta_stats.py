import sys
import mappy
import numpy as np


def collect_fasta_lengths(fasta_file):
    fasta_lengths = {}
    for name, seq, *_ in mappy.fastx_read(fasta_file):
        fasta_lengths[name] = len(seq)
    return fasta_lengths



def calculate_Nx(lengths) -> list[int]:
    """
    Calculate Nx values for this assembly

    :return: Nx values of the assembly
    """
    nx = []
    # sort sequence length and calc cumulative sum
    seq_lengths_sorted = np.sort(lengths)[::-1]
    seq_lengths_sorted_cuml = np.cumsum(seq_lengths_sorted)
    asm_perc = np.arange(0.01, 1.01, 0.01)
    # multiply either by total contig length
    # or by reference length/genome estimate
    asm_p = asm_perc * np.sum(lengths)
    for i in range(len(asm_p)):
        j = 0
        try:
            while seq_lengths_sorted_cuml[j] < asm_p[i]:
                j += 1
            nx.append(seq_lengths_sorted[j])
        except IndexError:
            nx.append(0)
    return nx




if __name__ == '__main__':
    flengths = collect_fasta_lengths(sys.argv[1])
    lens = list(flengths.values())
    nx = calculate_Nx(np.array(lens))
    stats = f"{len(lens)} contigs, total {sum(lens)} bp, min {min(lens)} bp, max {max(lens)} bp, avg {np.mean(lens)} bp, N50 {nx[49]} bp"
    print(stats)




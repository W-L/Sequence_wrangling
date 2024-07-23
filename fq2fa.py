import sys
import mappy



def fq2fa(fq_file):
    for name, seq, *_ in mappy.fastx_read(fq_file):
        print(f'>{name}\n{seq}')


if __name__ == '__main__':
    fq2fa(sys.argv[1])



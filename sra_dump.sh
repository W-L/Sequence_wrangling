# sensible arguments to download nanopore data. Because I can never remember them..
prefetch SRA
fastq-dump --gzip --readids --skip-technical --read-filter pass --clip $1 SRA/SRA.sra

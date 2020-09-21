# sensible arguments to download nanopore data. | SRR.... | target_dir
sra_dump() {fastq-dump --outdir $2 --gzip --readids --skip-technical --read-filter pass --clip $1; }

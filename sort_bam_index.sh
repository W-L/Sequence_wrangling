#! /bin/bash

# sorts, bamifies and indexes all files in a folder

files=$(ls *.$1)
samtools="/Volumes/Temp/Lukas/consensus_te/sw/samtools-1.6/samtools"

for f in $files; do
	f_base=$(basename $f .sam)
	echo $f_base

	bam="$samtools view -b $f -o $f_base.bam -@ 4"
	srt="$samtools sort $f_base.bam -o $f_base.sort.bam -@ 4"
	ind="$samtools index $f_base.sort.bam $f_base.sort.bam.bai -@ 4"
	
	eval "$bam"
	eval "$srt"
	eval "$ind"
done
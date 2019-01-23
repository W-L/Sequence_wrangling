#! /bin/bash


size=$(seq 150 100 2050)
step=$(seq 100 100 2000)

genome=../data/legionella_pneumophila_corby/legionella_genome.fasta
name=$(basename $genome)

mkdir -p processed

for i in $size
do
	for j in $step
	do
		if [ "$j" -le "$i" ]
		then
			Rscript ../code/GC_counter.R $genome $i $j && Rscript ../code/GC_plotter.R *$name.gc
			mv *.gc *.pdf processed
			echo "finished size $i and step $j"  
		fi	
	done	
done



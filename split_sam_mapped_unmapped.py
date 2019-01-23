#! /usr/local/bin/python3

# split a sam file into two: one with all mapped reads and one with all unmaped reads
    
import sys

def split(file_obj, mapped_obj, unmapped_obj):
    for line in file_obj:
        if line.startswith('@'):
            mapped_obj.write(line)
            unmapped_obj.write(line)
        else:            
            flag = int(line.split('\t')[1])
            if flag is 0 or flag is 16:
                mapped_obj.write(line)
            else:
                unmapped_obj.write(line)
                
                
file = open(sys.argv[1], 'r')
mapped = open(str(sys.argv[1]) + '.mapped.sam', 'w+')
unmapped = open(str(sys.argv[1]) + '.unmapped.sam', 'w+')

split(file, mapped, unmapped)

file.close()
mapped.close()
unmapped.close()

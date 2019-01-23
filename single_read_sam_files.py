#! /usr/local/bin/python3

# takes a sam file and writes every alignment to a new file
    
import sys

def singularize(file_obj):
    header = ''
    cnt = 1
    for line in file_obj:
        if line.startswith('@'):
            header = header + line
            
        else:            
            single = open(str(sys.argv[1]) + str(cnt) + '.sam', 'w+')                
            single.write(header)
            single.write(line)
            single.close()
            cnt += 1
            
file = open(sys.argv[1], 'r')

singularize(file)
file.close()

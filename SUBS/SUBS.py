#/usr/bin env python

import sys

dna_strings = sys.argv[1]
dna_strings = open(dna_strings, 'r')
dna_strings = dna_strings.readlines()

size1 = len(dna_strings[0].strip())
size2 = len(dna_strings[1].strip())

occurs = ''
print size1 - size2 , '\n'
for i in range(size1 - size2):
	for j in range(size2):
		if dna_strings[0][i+j] != dna_strings[1][j]: 
			break 
		if j == size2 - 1:
			occurs = occurs + str(i+1) + ' '
			

print occurs


#!/usr/bin env python

import sys

dna_strings = sys.argv[1]
dna_strings = open(dna_strings, 'r')
dna_strings = dna_strings.readlines()

hamm = 0

size = len(dna_strings[0])
for i in range(size):
    if dna_strings[0][i] != dna_strings[1][i]:
        hamm += 1

print hamm

#!/usr/bin env python
#! -*- coding:utf-8 -*-

import sys

replace_dict = {'A':'T' , 'C':'G' , 'T':'A' , 'G':'C'}

dna_string = sys.argv[1]
dna_string = open(dna_string, 'r')
dna_string = dna_string.read().strip()

rev_dna_string = dna_string[::-1]
rev_dna_string = list(rev_dna_string)

for i in range(len(rev_dna_string)):
  rev_dna_string[i] = replace_dict[rev_dna_string[i]]
  
print ''.join(rev_dna_string)



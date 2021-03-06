#!/usr/bin env python

import sys

codon_table = { 'UUU' :  'F'    , 'CUU' :  'L'   ,  'AUU':  'I'    ,  'GUU':  'V',
		'UUC' :  'F'     , 'CUC' :  'L'    , 'AUC':  'I'    ,  'GUC':  'V',
		'UUA' :  'L'     , 'CUA' :  'L'     ,'AUA':  'I'    ,  'GUA':  'V',
		'UUG' :  'L'     , 'CUG' :  'L'    , 'AUG':  'M'    ,  'GUG':  'V',
		'UCU' :  'S'     , 'CCU':  'P'     ,'ACU' :  'T'    , 'GCU':  'A',
		'UCC' :  'S'     , 'CCC':  'P'      ,'ACC':  'T'    ,  'GCC':  'A',
		'UCA' :  'S'     , 'CCA':  'P'      ,'ACA':  'T'   ,   'GCA':  'A',
		'UCG' :  'S'     , 'CCG':  'P'      ,'ACG':  'T'    ,  'GCG':  'A',
		'UAU' :  'Y'     , 'CAU':  'H'      ,'AAU':  'N'   ,   'GAU':  'D',
		'UAC' :  'Y'     , 'CAC':  'H'      ,'AAC':  'N'    ,  'GAC':  'D',
		'UAA' :  'Stop'  , 'CAA':  'Q'      ,'AAA':  'K'    ,  'GAA' :'E',
		'UAG' :  'Stop'  , 'CAG':  'Q'      ,'AAG':  'K'    ,  'GAG' :'E',
		'UGU':  'C'     , 'CGU':  'R'      ,'AGU' :  'S'    ,  'GGU': 'G',
		'UGC':  'C'     , 'CGC':  'R'      ,'AGC' :  'S'     , 'GGC': 'G',
		'UGA' :  'Stop' ,  'CGA':  'R'      ,'AGA':  'R'    ,  'GGA' :'G',
		'UGG':  'W'    ,  'CGG':  'R'   ,   'AGG':  'R'   ,   'GGG' :'G' }


dna_string = sys.argv[1]
dna_string = open(dna_string, 'r')
dna_string = dna_string.read().strip()
dna_string = list(dna_string)

size = len(dna_string)

protein = ''
i = 0
while i < size:
   amino_acid = dna_string[i] + dna_string[i+1] + dna_string[i+2]
   protein = protein + codon_table[amino_acid]
   i+= 3

print protein	


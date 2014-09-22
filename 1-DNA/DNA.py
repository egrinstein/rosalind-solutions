#!/usr/bin env python
#! -*- coding:utf-8 -*-

ocurrences = {'A':0 , 'C':0 , 'G':0 , 'T':0}

dna_string = raw_input("Name of the file containing the DNA string:")
dna_string = open(dna_string,'r')
dna_string = dna_string.read().strip()

for symbol in dna_string:
   ocurrences[symbol] += 1

for symbol in ocurrences:
   print ocurrences[symbol]


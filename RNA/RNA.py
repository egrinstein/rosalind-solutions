#!/usr/bin env python
#! -*- coding:utf-8 -*-

rna_string = raw_input("Name of the RNA string file:")
rna_string = open(rna_string,'r')
rna_string = rna_string.read().strip()

dna_string = rna_string.replace('T','U')

print dna_string


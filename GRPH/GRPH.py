#!/usr/bin env python

from Bio import SeqIO

handle = open("input.fasta", "rU")
record_list = SeqIO.parse(handle,"fasta")

nodes = {}
for record in record_list:
    nodes[str(record.id.strip())] = {'seq':record.seq.strip()}


for node_from in nodes.keys():
    for node_to in nodes.keys():
        if str(node_from) != str(node_to):
            if str(nodes[node_from]['seq'][-3:]) == str(nodes[node_to]['seq'][:3]):
              print node_from+' '+node_to


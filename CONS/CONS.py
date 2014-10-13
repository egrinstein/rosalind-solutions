from Bio import SeqIO
import numpy

def generate_profile(fasta_filename, length):
  handle = open(fasta_filename, "rU")
  record_list = SeqIO.parse(handle,"fasta")

  profile = {"A": 10*[0],
             "C": 10*[0],
             "G": 10*[0],
             "T": 10*[0]}


  for record in record_list:
    i = 0
    length = len(record.seq)
    for base in record:
      profile[base][i] += 1
      i+=1
  return profile

a = 0
generate_profile("input.fasta",a)


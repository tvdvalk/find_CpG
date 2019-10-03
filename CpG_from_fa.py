#!/usr/bin/python
from __future__ import division
from Bio import SeqIO
import operator
from sys import argv
import math

"""
Tom van der Valk
tvdvalk1989@gmail.com
Script to identify CpG sites in a haploid fasta reference
Output is in BED-format
usage = CpG_from_fa.py reference.fa output_filename
"""

def find_cpg(reference,outputname):

    outputfile = open(outputname + ".bed", "w")
    fasta_sequences = SeqIO.parse(open(reference),'fasta')
    for fasta in fasta_sequences:
        name, sequence = fasta.id, str(fasta.seq).upper()
        for i in range(len(sequence)-1):
            position = i
            if (sequence[i] + sequence[i+1]) == "CG":
                outputfile.write(name + "\t" + str(position) + "\t" + str(position + 1) + "\n")

    outputfile.close()

if __name__ == "__main__":
    find_cpg(argv[1],argv[2])

from Bio import Entrez
from Bio import SeqIO
import os

Entrez.email = "Dan.Vanatta@gmail.com"
input_data = open("rosalind_need.txt").read().rstrip()
ids=input_data.replace(" ", ", ")
handle = Entrez.efetch(db="nucleotide", id=[ids], rettype="fasta")
records = list(SeqIO.parse(handle, "fasta"))
for i in records:
    print i.seq
SeqIO.write(records[0], "need1.faa", "fasta")
SeqIO.write(records[1], "need2.faa", "fasta")

os.system("needle need1.faa need2.faa -gapopen 10 -gapextend 1 -outfile need_output.txt -endweight true -endopen 10 -endextend 1")

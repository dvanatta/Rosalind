from Bio import Entrez
from Bio import SeqIO


Entrez.email = "Dan.Vanatta@gmail.com"
input_data = open("rosalind_frmt.txt").read().rstrip()
ids=input_data.replace(" ", ", ")
handle = Entrez.efetch(db="nucleotide", id=[ids], rettype="fasta")
records = list(SeqIO.parse(handle, "fasta"))
maxlen = 10000000
for i in records:
    if len(i.seq) < maxlen:
        longest_seq = i
        maxlen=len(i.seq)
print ">"+longest_seq.description
print longest_seq.seq
SeqIO.write(longest_seq, "example.faa", "fasta") 

from Bio import Entrez


Entrez.email = "Dan.Vanatta@gmail.com"
input_data = open('rosalind_gbk.txt').read().split()
searchterm = input_data[0]
startdate = input_data[1]
stopdate = input_data[2]
handle = Entrez.esearch(db="nucleotide", term=searchterm+'[Organism]', mindate=startdate, maxdate=stopdate, datetype="pdat")
record = Entrez.read(handle)
print record

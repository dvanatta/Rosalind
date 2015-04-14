from Bio.Seq import translate

filename = "rosalind_ptra.txt"
dna_list = []
for line in open(filename):
    dna_list.append(line.rstrip())
translated_string = ""
i=1
while i <=6:
    translated_string = translate(dna_list[0], to_stop=True,table = str(i) )
    print translated_string, dna_list[-1]
    if translated_string == dna_list[-1]:
        print i
        break 
    i+=1

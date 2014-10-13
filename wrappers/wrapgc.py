import parser
import dna

dataset = parser.parse_rosalind("ex5.txt")
gcmax = 0
name = ''

for i in range(len(dataset)):
    gc = dna.calculate_gc(dataset[i][1])
    if gc > gcmax:
        gcmax = gc
        name = dataset[i][0]
print name
print gcmax

import dna
import parser

dna_array = dna.vert(parser.parse_fasta("rosalind_splc.txt"),1)

print dna.splice(dna_array)

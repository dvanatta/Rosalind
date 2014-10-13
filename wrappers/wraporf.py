import dna
import parser

seq = parser.parse_fasta("rosalind_orf.txt")[0][1]

output = dna.open_reading_frame(seq)

for i in output:
    print i

import dna_parser


input = dna_parser.parse_fasta("rosalind_sseq.txt")
#input = parser.parse_fasta("ex23.txt")
s = input[0][1]
t = input[1][1]
output = dna.spliced_motif(s,t)
print ' '.join(str(i) for i in output)

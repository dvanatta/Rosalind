import dna
import parser

#array = parser.rosa_from_txt('ex16.txt')
#array = parser.rosa_from_txt('/Users/Dan/Downloads/rosalind_mprt.txt')
seq = parser.parse_fasta('/home/dvanatta/Downloads/rosalind_revp.txt')[0][1]
#seq = parser.parse_fasta('ex17.txt')[0][1]
print len(seq)

repr(dna.res_site(seq))

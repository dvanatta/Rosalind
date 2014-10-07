import dna
import parser

#array = parser.rosa_from_txt('ex16.txt')
array = parser.rosa_from_txt('/Users/Dan/Downloads/rosalind_mprt.txt')
seqs = dna.vert(array,1)
for i in range(len(seqs)):
    result = dna.glyco_motif(seqs[i])
    if result:
        print array[i][0]
        print ' '.join(str(num) for num in result)
#        print dna.glyco_motif(seqs[i])

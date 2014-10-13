import dna
import parser

seq = parser.parse_fasta("rosalind_kmp.txt")[0][1]
print len(seq)
output = dna.kmp_fail(seq)

print ' '.join(str(a) for a in output)


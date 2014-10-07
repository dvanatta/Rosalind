import parser
import dna

seq = parser.parse_txt('/home/dvanatta/Downloads/rosalind_prtm.txt')
print seq
print dna.mass_p(seq)

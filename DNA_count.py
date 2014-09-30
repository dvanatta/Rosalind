import numpy
import dna
import parser

#write an arg_parser to take command line inputs for this
#input = parser.parse_txt('/Users/Dan/Downloads/rosalind_subs.txt')
input = parser.parse_rosalind('ex10.txt')
#print dna.motif(input[0],input[1])

#block = [row[1] for row in input]
output = dna.consensus(input)
print "A:", ' '.join(str(n) for n in output[0])
print "C:", ' '.join(str(n) for n in output[1])
print "G:", ' '.join(str(n) for n in output[2])
print "T:", ' '.join(str(n) for n in output[3])

#print dna.translate(input)
#print dna.calculate_hamming(input[0], input[1])	

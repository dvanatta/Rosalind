import numpy
import dna
import parser

#write an arg_parser to take command line inputs for this
input = parser.parse_rosalind('/Users/Dan/Downloads/rosalind_grph.txt')
#input = parser.parse_rosalind('ex12.txt')
#column = [row[1] for row in input]

edges = dna.overlap(input)

for i in range(len(edges)):
    print edges[i][0], edges[i][1]

import dna_parser
import dna


#sequence = dna_parser.parse_numbers("rosalind_lgis.txt")[1]
sequence = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5,13, 3, 11, 7,15] 


print longest_decreasing_subseq(sequence, "dec")
print longest_decreasing_subseq(sequence, "inc")


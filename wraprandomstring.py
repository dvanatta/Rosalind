import parser
import dna

input = parser.parse_txt('rosalind_prob.txt')
seq = input[0]
probs = input[1].split()
for i in range(len(probs)):
    probs[i] = float(probs[i])
print dna.random_string(seq,probs)
print seq, probs

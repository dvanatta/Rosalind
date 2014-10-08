#start with loop with shortest length
#check every other string for full match
#break if not match
#repeat with shortest loop - 1

import parser
import dna
dna_array = dna.vert(parser.parse_rosalind("rosalind_lcsm.txt"),1)
#dna_array = dna.vert(parser.parse_rosalind("ex13.txt"),1)


def has_motif(dna,sub):
    for i in range(len(dna)-len(sub)+1):
        if dna[i:i+len(sub)] == sub:
            return True
    return False


def check_motifs(dna_array,substring):
    glob_match = True 
    for dna in dna_array:
        local_match = has_motif(dna,substring)
        if local_match:
            pass
        else:
            glob_match = False
        if local_match == False:
            break
    if glob_match == True:
            return substring

            
def enumerate_substrings(dna_array):
    substring = []
    shortest_dna = dna_array[0]
    for i in range(len(dna_array)):
        if len(shortest_dna) > len(dna_array[i]):
            shortest_dna = dna_array[i]
    for n in reversed(range(len(shortest_dna))): 
        sub_len= n + 1 
        substring.append([])
        for j in range(len(shortest_dna)-n): # number of possibilities based on substring length
            sub = check_motifs(dna_array,shortest_dna[j:j+sub_len])
            if sub:
                return sub 

#print check_motifs(dna_array,substrings)
print enumerate_substrings(dna_array)

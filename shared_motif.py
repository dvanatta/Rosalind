#starti with loop with shortest length
#check every other string for full match
#break if not match

#for each substring need to be a double loop over the number of strings and the number of posible pairings = (len(string)-len(substring)+1)
import parser
import dna
dna_array = dna.vert(parser.parse_rosalind("rosalind_lcsm.txt"),1)
#dna_array = dna.vert(parser.parse_rosalind("ex13.txt"),1)

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
            substring[len(shortest_dna)-sub_len].append(shortest_dna[j:j+sub_len])

    return substring 

substrings = enumerate_substrings(dna_array)        
print substrings

def check_motif(s,t):
    for i in range(len(s)-len(t)+1):
        if s[i:i+len(t)] == t:
            return True
    return False

def check_motifs(dna_array,substrings):
    for n in substrings:
        for sub in n:
            glob_match = True 
            for dna in dna_array:
                local_match = check_motif(dna,sub)
                if local_match:
                    pass
                else:
                    glob_match = False
                if local_match == False:
                     break
            if glob_match == True:
                    return sub
            

print check_motifs(dna_array,substrings)

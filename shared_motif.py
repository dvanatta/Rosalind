#starti with loop with shortest length
#check every other string for full match
#break if not match

#for each substring need to be a double loop over the number of strings and the number of posible pairings = (len(string)-len(substring)+1)
import parser
import dna
dna_array = dna.vert(parser.parse_rosalind("rosalind_lcsm.txt"),1)
#dna_array = dna.vert(parser.parse_rosalind("ex13.txt"),1)

#start with dna_array
#this function isn't even finishing, i guess in a real dataset it's not feasible to enumrate all substrings
def enumerate_substrings(dna_array):
#   break this into separate function "enumerate_subsrings", possibly with some logic to check for uniqueness? that might take longer than just running the double seq in many case
    substring = []
    shortest_dna = dna_array[0]
    for i in range(len(dna_array)):
        if len(shortest_dna) > len(dna_array[i]):
            shortest_dna = dna_array[i]
    # loop over substring lengths
    for n in reversed(range(len(shortest_dna))): #len shortest_dna is longest possible substring)
        sub_len= n + 1 
        substring.append([])
        #loop over dna_array
#        for i in range(len(dna_array)):
            #loop over possible substrings
        for j in range(len(shortest_dna)-n): # number of based on substring length
                substring[len(shortest_dna)-sub_len].append(shortest_dna[j:j+sub_len])
    return substring 

substrings = enumerate_substrings(dna_array)        
print substrings

def check_motif(s,t):
    for i in range(len(s)-len(t)+1):
#        print "s,t", s[i:i+len(t)],t
        if s[i:i+len(t)] == t:
            return True
    return False

#enumerate subsrings sems to work ok, just need to figure out how to keep track of global and local matches
def check_motifs(dna_array,substrings):
    for n in substrings:
#        print "len n= ", len(n), n
        for sub in n:
#            print "sub=", sub
            glob_match = True 
            for dna in dna_array:
#                print "dna=", dna
#                local_match = False
#                print sub, dna
                local_match = check_motif(dna,sub)
                if local_match:
#                    print "found a match"
                    pass
                else:
#                    print "no match in this dna"
                    glob_match = False
                if local_match == False:
#                     glob_match == False
                     break
            if glob_match == True:
#                    print "win!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!", sub
                    return sub
                
            

#                match = False
               # for k in range(len(dna_array)): #loop over all dnas
                   # if dna_array[j][k:k+sub_len] == substring:
                    #    match = True
#                        pass
#                if match == False: #if there isn't a match in this dna, no need to check the others.
#                    break
#    return longest_substring


print check_motifs(dna_array,substrings)

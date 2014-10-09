#move tables to separate file or global variales
#Make sure all scripts end up in here ie shared motifs.py and delete when added
# should probably refactor all of this to use real 2D arrays instea of this nested list crap
# library of simple functions for bioinformatics analysis DKV 9/2014
# this library should focus on functions which take dna string as input
#TODO assert statements on input and output and/or duck typing
#good comments
#use each rosalind problem as a unit test case for these functions
# should probably rework dna/rna into a class
#could be refactored to make use of numpy and real 2D arrays but that's cheating!
#turn this into nucleic acid class
import math

def count(dna):
#input DNA string, returns count of of each nucleic acid
    A, T, C, G = 0, 0, 0, 0
    for nuc in dna:
        if nuc == 'A':
            A += 1
        if nuc == 'C':
            C += 1
        if nuc == 'G':
            G += 1
        if nuc == 'T':
            T += 1
    return A, C, G, T


def complement_nuc(nuc, strand="dna"):
#input nucleic acid, returns RNA complement
    if nuc == 'G':
         return 'C'
    if nuc == 'C':
        return 'G'
    if nuc == 'T':
        return 'A'

    if strand == 'dna':
        if nuc == 'A':
            return 'T'

    if strand == 'rna':
        if nuc == 'A':
           return 'U'


#DEPRECAED USE rev_comp instead
def to_dna(dna):
#input dna returns reverse complement DNA
    print "Deprecated, use rev_comp instead"
    dna_complement = ''
    for nuc in reversed(dna):
        dna_complement += complement_nuc(nuc)
    return dna_complement


def comp(dna, string = "dna"):
    dna_comp = ''
    for nuc in dna:
        dna_comp += complement_nuc(nuc, string)
    return dna_comp


def rev_comp(dna, string="rna"):
#input dna returns reverse complement. select "dna" or "rna"
    rna =''
    for nuc in reversed(dna):
        rna += complement_nuc(nuc, string)
    return rna


def to_rna_sense(dna):
#input dna returns corresponding RNA senselike (ie replaces T with U keep order)
    rna = ''
    for nuc in dna:
        if nuc == 'T':
            rna += 'U'
        else:
            rna += nuc
    return rna


def calculate_gc(dna):
# input seq return percentage GC
    count = 0.0
    for nuc in dna:
        if nuc == 'G' or nuc == 'C':
            count +=1
    return count / len(dna)


def calculate_hamming(dna1, dna2):
# input two seq returns hamming score
    hamming = 0.0
    lendna1 = len(dna1)
    lendna2 = len(dna2)
    short_strand = min(lendna1, lendna2)
    for i in range(short_strand):
        if dna1[i] != dna2[i]:
            hamming += 1
    hamming += abs(lendna1-lendna2) # add length diff to score
    return hamming


def translate(rna):
#input rna seq returns protein seq
    protein = ''
    codon_table = {"UUU":"F", "UUC":"F", "UUA":"L", "UUG":"L",
       "UCU":"S", "UCC":"S", "UCA":"S", "UCG":"S",
       "UAU":"Y", "UAC":"Y", "UAA":"", "UAG":"",
       "UGU":"C", "UGC":"C", "UGA":"", "UGG":"W",
       "CUU":"L", "CUC":"L", "CUA":"L", "CUG":"L",
       "CCU":"P", "CCC":"P", "CCA":"P", "CCG":"P",
       "CAU":"H", "CAC":"H", "CAA":"Q", "CAG":"Q",
       "CGU":"R", "CGC":"R", "CGA":"R", "CGG":"R",
       "AUU":"I", "AUC":"I", "AUA":"I", "AUG":"M",
       "ACU":"T", "ACC":"T", "ACA":"T", "ACG":"T",
       "AAU":"N", "AAC":"N", "AAA":"K", "AAG":"K",
       "AGU":"S", "AGC":"S", "AGA":"R", "AGG":"R",
       "GUU":"V", "GUC":"V", "GUA":"V", "GUG":"V",
       "GCU":"A", "GCC":"A", "GCA":"A", "GCG":"A",
       "GAU":"D", "GAC":"D", "GAA":"E", "GAG":"E",
       "GGU":"G", "GGC":"G", "GGA":"G", "GGG":"G",}
    for i in range(len(rna)/3):
        ind = 3*i
        protein += codon_table[rna[ind]+rna[ind + 1]+rna[ind + 2]]
    return protein.rstrip()


def motif(s,t):
#input string, substring returns index of all matches
    matches = []
    for i in range(len(s)):
        if s[i:i+len(t)] == t:
            matches.append(i+1)
    return matches


def consensus(input):
#input in rosalind array, returns consensus sequence and score_matrix
    dna_array = []
    for i in input:
        dna_array.append(i[1])  
    N = len(dna_array[0])
    #this is similar to count block i should probably call it
    scores = [[0]*N, [0]*N, [0]*N, [0]*N]
    for i in range(len(dna_array)):
        for j in range(len(dna_array[i])):
            if dna_array[i][j] == "A":
                scores[0][j] += 1
            if dna_array[i][j] == "C":
                scores[1][j] += 1
            if dna_array[i][j] == "G":
                scores[2][j] += 1
            if dna_array[i][j] == "T":
                scores[3][j] += 1
    #this should maybe be it's own function aka "score"
    seq =''
    for i in range(N):
        block = [row[i] for row in scores]
        nuc = block.index(max(block))
        if nuc == 0:
            seq += "A"
        if nuc == 1:
            seq += "C"
        if nuc == 2:
            seq += "G"
        if nuc == 3:
            seq += "T"
    return seq, scores            


def vert(array,i):
#input array and column number, returns column as list
    column = [row [i] for row in array]
    return column

    
def overlap(rosalind_array, k=3):
#input 2d rosalind array and option k, returns edges where suffix s matches prefix of t to k places
    dna_array = vert(rosalind_array, 1) 
    edges = []
    for i in range(len(dna_array)):
        for j in range(len(dna_array)):
            if i != j:
                if dna_array[i][-k:len(dna_array[i])] == dna_array[j][0:k]:
                    edges.append([rosalind_array[i][0], rosalind_array[j][0]])
    return edges


def glyco_motif(seq):
#input seq, returns all locations of glycosolation motif
#optimization? : find all N * [ST] *, then delete all matches containing a P
    locations = []
    for i in range(len(seq)-4):
        if seq[i] == 'N' and seq[i+1] != 'P' and (seq[i+2] == 'S' or seq[i+2] == 'T') and seq[i+3] != 'P':
            locations.append(i+1)
    return locations


#Should try to generalize this for N length palindromes, also store output instead of print
def res_site(seq):
#input seq, locates restriction sites (ie reservse palindromes of lengths 4-12)
    seqB = comp(seq, "dna")
    print seq, seqB
    for i in range(len(seq)-11):
        if seq[i] == seqB[i+11] and seq[i+1] == seqB[i+10] and seq[i+2] == seqB[i+9] and seq[i+3] == seqB[i+8] and seq[i+4] == seqB[i+7] and seq[i+5] == seqB[i+6]:    
            print i+1, "12"
    for i in range(len(seq) - 9):
        if seq[i] == seqB[i+9] and seq[i+1] == seqB[i+8] and seq[i+2] == seqB[i+7] and seq[i+3] == seqB[i+6] and seq[i+4] == seqB[i+5]:
            print i+1, "10"
    for i in range(len(seq)-7):
        if seq[i] == seqB[i+7] and seq[i+1] == seqB[i+6] and seq[i+2] == seqB[i+5] and seq[i+3] == seqB[i+4]:
            print i+1, "8"    
    for i in range(len(seq)-5):
        if seq[i] == seqB[i+5] and seq[i+1] == seqB[i+4] and seq[i+2] == seqB[i+3]:
            print i+1, "6"    
    for i in range(len(seq)-3):
        if seq[i] == seqB[i+3] and seq[i+1] == seqB[i+2]:
            print i+1, "4"    
       

def mass_p(seq):
#input protein returns mass
    mass_table = {
    'A': 71.03711,
    'C': 103.00919,
    'D': 115.02694,
    'E': 129.04259,
    'F': 147.06841,
    'G': 57.02146,
    'H': 137.05891,
    'I': 113.08406,
    'K': 128.09496,
    'L': 113.08406,
    'M': 131.04049,
    'N': 114.04293,
    'P': 97.05276,
    'Q': 128.05858,
    'R': 156.10111,
    'S': 87.03203,
    'T': 101.04768,
    'V': 99.06841,
    'W': 186.07931,
    'Y': 163.06333,
}
    total_mass = 0
    for i in seq:
        total_mass += mass_table[i]
    return total_mass 


def enum_rna(seq):
#input seq, returns numbers of possible mra % 1000000
    amino_codon_table = {
    "A" : 4,
    "R" : 6,
    "D" : 2,
    "N" : 2,
    "C" : 2,
    "E" : 2,
    "Q" : 2,
    "G" : 4,
    "H" : 2,
    "I" : 3,
    "L" : 6,
    "K" : 2,
    "M" : 1,
    "F" : 2,
    "P" : 4,
    "S" : 6,
    "T" : 4,
    "W" : 1,
    "Y" : 2,
    "V" : 4,
}
    total = 3 #start at 3 because of stop codons
    for i in range(len(seq)):
        total *=  amino_codon_table[seq[i]]
    return total % 1000000


def has_motif(dna,sub):
#input dna and substring, checks if substring is in this dna
    for i in range(len(dna)-len(sub)+1):
        if dna[i:i+len(sub)] == sub:
            return True
    return False


def check_motifs(dna_array,substring):
#input array of dna and a substring, returns substring if substring is in all dna
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


#start with loop with shortest length
#check every other seq for full match
#break if not match in seq
#repeat with shortest loop - 1
#would it be quicker to loop starting from the smallest? probably depends on the data set.  try it on rosalind
def longest_common_shared_motif(dna_array):
#input array of dna, returns longest common substring
    shortest_dna = dna_array[0]
    for i in range(len(dna_array)):
        if len(shortest_dna) > len(dna_array[i]):
            shortest_dna = dna_array[i]
    len_shortest = len(shortest_dna)
    for n in reversed(range(len_shortest)): 
        for j in range(len_shortest-n): # number of possibilities based on substring length
            sub = check_motifs(dna_array,shortest_dna[j:j+n+1])
            if sub:
                return sub 


#i dont think this will work if there is more than one substring match because the loop will go wonky after the splice.  fix by appending good dna to a diff string
def splice(dna_array):
#input array of [dna, substring1, substring2...]. splices out all substrings then transcribes and translates to return protein
    dna = dna_array[0]
    len_dna = len(dna)
    spliced_dna = ''
    for i in range(len(dna_array)-1):
        substring = dna_array[i+1]
        len_sub = len(substring)
        for i in range(len_dna-len_sub):
            if dna[i:i+len_sub] == substring:
                dna = dna[0:i]+dna[i+len_sub:len(dna)]
                i = i + len_sub
    return translate(to_rna_sense(dna))


def random_string(seq,probs):
    len_probs = len(probs)
    output = [0]*len_probs
    gc = calculate_gc(seq)
    for i in range(len_probs):
        pg = math.log10(probs[i]/2)
        pt = math.log10((1-probs[i])/2)
        for j in seq:
            if j == 'A' or j == 'T':
                output[i] += pt
            else:
                output[i] += pg 
    return output 

# should probably refactor all of this to use real 2D arrays instea of this nested list crap
# library of simple functions for bioinformatics analysis DKV 9/2014
# this library should focus on functions which take dna string as input
#TODO assert statements on input and output and/or duck typing
#good comments
#use each rosalind problem as a unit test case for these functions
# should probably rework dna/rna into a class
#could be refactored to make use of numpy and real 2D arrays but that's cheating!
#turn this into nucleic acid class

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
# input dna return percentage GC
    count = 0.0
    for nuc in dna:
        if nuc == 'G' or nuc == 'C':
            count +=1
    return count / len(dna) * 100

def calculate_hamming(dna1, dna2):
#if strings are mismatch lengths treat add the difference to score
    hamming = 0.0
    lendna1 = len(dna1)
    lendna2 = len(dna2)
    short_strand = min(lendna1, lendna2)
    for i in range(short_strand):
        if dna1[i] != dna2[i]:
            hamming += 1
    hamming += abs(lendna1-lendna2)
    return hamming


def translate(rna):
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
    #optimization : find all N * [ST] *, then delete all matches containing a P
    locations = []
    for i in range(len(seq)-4):
        if seq[i] == 'N' and seq[i+1] != 'P' and (seq[i+2] == 'S' or seq[i+2] == 'T') and seq[i+3] != 'P':
            locations.append(i+1)
    return locations



#Should try to generalize this for N length palindromes..  
def res_site(seq):
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


       

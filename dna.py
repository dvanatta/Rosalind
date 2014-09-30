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
#input in rosalind array
    dna_array = []
    for i in input:
        dna_array.append(i[1])  
        print dna_array
    N = len(dna_array[0])
    output = [[0]*N, [0]*N, [0]*N, [0]*N]
    for i in range(len(dna_array)):
        for j in range(len(dna_array[i])):
            if dna_array[i][j] == "A":
                output[0][j] += 1
            if dna_array[i][j] == "C":
                output[1][j] += 1
            if dna_array[i][j] == "G":
                output[2][j] += 1
            if dna_array[i][j] == "T":
                output[3][j] += 1
#    for i in range(len(N)):
#        nuc = max (output[i]    
    return output            
 #   for i in range(len(dna_array[0])):
 #       countA, countC, countG, countT = 0, 0, 0, 0
 #       block = [row[i] for row in dna_array]
 #       print block, count(block)




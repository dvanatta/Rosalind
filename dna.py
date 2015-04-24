"""
Functions for bioinformatics analysis DKV 9/2014
https://github.com/dvanatta/Rosalind

Notes
-----
Focus on functions which take dna string as input
Use each rosalind problem as a unit test case for these functions

TODO
----
Move tables to separate file or global variales
Could refactor all of this to use real 2D numpy arrays
"""
import math


def count(dna):
    """
    Counts occurences of each nucleotide in DNA

    Parameters
    ----------
    dna : str
        Input sequence of nucelotides

    Returns
    -------
    counts : dict
         Count of each nucleotide
    """
    counts = {"A": 0, "C": 0, "G": 0, "T": 0}
    for nuc in dna:
        counts[nuc] += 1
    return counts["A"], counts["C"], counts["G"], counts["T"]


def complement_nuc(nuc, strand="dna"):
    """
    Complement a nucleotide

    Parameters
    ----------
    nuc : str
        Input nucelotide
    strand : "dna" or "rna"
        Choose output strand type

    Returns
    -------
    str
    Corresponding nucleotide
    """
    complements_dna = {"G": "C", "C": "G", "T": "A", "A": "T"}
    complements_rna = {"G": "C", "C": "G", "T": "A", "A": "U"}
    if strand == 'dna':
        return complements_dna[nuc]
    elif strand == 'rna':
        return complements_rna[nuc]
    else:
        print "Couldn't find a complement"


def rev_comp(dna, strand="rna"):
    """
    Returns reverse complement nucleic acid

    Parameters
    ----------
    dna : str
        Input sequence of nucelotides
    strand : "dna" or "rna"
        Choose output strand type

    Returns
    -------
    rna : str
         Strand reversed and complement to input
    """
    rna = []
    for nuc in reversed(dna):
        rna.append(complement_nuc(nuc, strand))
    rna = ''.join(map(str, rna))
    return rna


def comp(dna, strand="dna"):
    """
    Returns complement nucleic acid

    Parameters
    ----------
    dna : str
        Input sequence of nucelotides
    strand : "dna" or "rna"

    Returns
    -------
    dna_comp : str
         Strand complement to input
    """
    dna_comp = []
    for nuc in dna:
        dna_comp.append(complement_nuc(nuc, strand))
    dna_comp = ''.join(map(str, dna_comp))
    return dna_comp


def to_rna_sense(dna):
    """
    Returns rna sense strand corresponding to input DNA
    In other words, replace T with U

    Parameters
    ----------
    dna : str
        Input sequence of nucelotides

    Returns
    -------
    rna : str
        rna sense strand
    """
    rna = []
    for nuc in dna:
        if nuc == 'T':
            rna.append('U')
        else:
            rna.append(nuc)
    rna = ''.join(map(str, rna))
    return rna


def calculate_gc(dna):
    """
    Calculate the GC content of a nucleic acid

    Parameters
    ----------
    dna : str
        Input sequence of nucelotides

    Returns
    -------
    float
        Percent of the strand made up of G or C
    """
    count = 0.0
    for nuc in dna:
        if nuc == 'G' or nuc == 'C':
            count += 1
    return count / len(dna)


def calculate_hamming(dna1, dna2):
    """
    Calculates the hamming score from aligning two sequences
    Each nucleic acid mismatch contributes 1 to the score
    Difference in sequence legnth is also added

    Parameters
    ----------
    dna1, dna2 : str
        Input sequences of nucelotides

    Returns
    -------
    hamming : int
         Hamming score
    """
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
    """
    Translates rna sequence into amino acids
    Doesn't return if no stop codon (simplifies open_reading_frames)

    Parameters
    ----------
    rna : str
        Input sequence of nucelotides

    Returns
    -------
    protein : str
         Sequence of amino acids
    """
    protein = ''
    codon_table = {
        "UUU": "F", "UUC": "F", "UUA": "L", "UUG": "L",
        "UCU": "S", "UCC": "S", "UCA": "S", "UCG": "S",
        "UAU": "Y", "UAC": "Y", "UAA": "", "UAG": "",
        "UGU": "C", "UGC": "C", "UGA": "", "UGG": "W",
        "CUU": "L", "CUC": "L", "CUA": "L", "CUG": "L",
        "CCU": "P", "CCC": "P", "CCA": "P", "CCG": "P",
        "CAU": "H", "CAC": "H", "CAA": "Q", "CAG": "Q",
        "CGU": "R", "CGC": "R", "CGA": "R", "CGG": "R",
        "AUU": "I", "AUC": "I", "AUA": "I", "AUG": "M",
        "ACU": "T", "ACC": "T", "ACA": "T", "ACG": "T",
        "AAU": "N", "AAC": "N", "AAA": "K", "AAG": "K",
        "AGU": "S", "AGC": "S", "AGA": "R", "AGG": "R",
        "GUU": "V", "GUC": "V", "GUA": "V", "GUG": "V",
        "GCU": "A", "GCC": "A", "GCA": "A", "GCG": "A",
        "GAU": "D", "GAC": "D", "GAA": "E", "GAG": "E",
        "GGU": "G", "GGC": "G", "GGA": "G", "GGG": "G"
        }
    for i in range(len(rna)/3):
        ind = 3*i
        codon = codon_table[rna[ind]+rna[ind + 1]+rna[ind + 2]]
        protein += codon
        if codon == "":
            return protein.rstrip()


def motif(s, t):
    """
    Finds index of all occurences of substring in string

    Parameters
    ----------
    s: str
        Input sequence
    t:  str
        input subsequence

    Returns
    -------
    matches : list (of ints)
         Index of each full substring match
    """
    matches = []
    for i in range(len(s)-len(t)+1):
        if s[i:i+len(t)] == t:
            matches.append(i+1)
    return matches


# this might be simpler with a dict also
def consensus(input):
    """
    Compares multiple sequences to determine consensus seq and profile matrix

    Parameters
    ----------
    input : list
        2xN list of [[label, sequence]...]

    Returns
    -------
    scores : list
        4xlen(seq) list of count of each nucleotide at each position
    seq: str
        Consensus sequence from max score at each position
    """
    dna_array = []
    for i in input:
        dna_array.append(i[1])
    N = len(dna_array[0])
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
    seq = ''
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


def vert(array, i):
    """
    Extract a column from an array

    Parameters
    ----------
    array : list (of lists)
        Python array that wishes it was a numpy array
    i : int
        Index of column to extract

    Returns
    -------
    Column : list
         Column at index i of matrix
    """
    column = [row[i] for row in array]
    return column


def overlap(rosalind_array, k=3):
    """
    Calculates overlap graph for a collection of seqs
    Define edge between s, t where suffix of s matches prefix of t to k places

    Parameters
    ----------
    rosaling_array : list
        2xN list of [[label, sequence]...]
    k : int
        Match length to define edge

    Returns
    -------
    edges : list (of lists of strings)
        Directed pairs of labels [s, t]
    """
    dna_array = vert(rosalind_array, 1)
    edges = []
    for i in range(len(dna_array)):
        for j in range(len(dna_array)):
            if i != j:
                if dna_array[i][-k:len(dna_array[i])] == dna_array[j][0:k]:
                    edges.append([rosalind_array[i][0], rosalind_array[j][0]])
    return edges


# optimization? : find all N * [ST] *, then delete all matches containing a P
def glyco_motif(seq):
    """
    Finds all occurences of glycosolation motif

    Parameters
    ----------
    seq : str
        Input sequence of nucelotides

    Returns
    -------
    locations : list (of ints)
         Index of each glycosolation motif
    """
    locations = []
    for i in range(len(seq)-4):
        if (
            seq[i] == 'N' and seq[i+1] != 'P' and
            (seq[i+2] == 'S' or seq[i+2] == 'T') and seq[i+3] != 'P'
                ):
            locations.append(i+1)
    return locations


# TODO
# Should try to generalize this for N length palindromes
# store output instead of print
def res_site(seq):
    """
    Finds restriction sites (reverse palindromes length 4-12)

    Parameters
    ----------
    seq : str
        Input sequence of nucelotides

    Returns
    -------
    location and length of each restriction site
    """
    seqB = comp(seq, "dna")
    print seq, seqB
    for i in range(len(seq)-11):
        if (seq[i] == seqB[i+11] and seq[i+1] == seqB[i+10] and
            seq[i+2] == seqB[i+9] and seq[i+3] == seqB[i+8] and
                seq[i+4] == seqB[i+7] and seq[i+5] == seqB[i+6]):
            print i+1, "12"
    for i in range(len(seq) - 9):
        if (seq[i] == seqB[i+9] and seq[i+1] == seqB[i+8] and
            seq[i+2] == seqB[i+7] and seq[i+3] == seqB[i+6] and
                seq[i+4] == seqB[i+5]):
            print i+1, "10"
    for i in range(len(seq)-7):
        if (seq[i] == seqB[i+7] and seq[i+1] == seqB[i+6] and
                seq[i+2] == seqB[i+5] and seq[i+3] == seqB[i+4]):
            print i+1, "8"
    for i in range(len(seq)-5):
        if (seq[i] == seqB[i+5] and seq[i+1] == seqB[i+4] and
                seq[i+2] == seqB[i+3]):
            print i+1, "6"
    for i in range(len(seq)-3):
        if seq[i] == seqB[i+3] and seq[i+1] == seqB[i+2]:
            print i+1, "4"


def mass_p(seq):
    """
    Sums mass of each amino acid to determine mass of protein

    Parameters
    ----------
    seq : str
        Input sequence of amino acids

    Returns
    -------
    total_mass : float
         mass of protein in amu
    """
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
    """
    Calculate how many sequences could have coded this protein sequence

    Parameters
    ----------
    seq : str
        Input sequence of amino acids

    Returns
    -------
    total: int
         number of coding strands % 1000000
    """
    amino_codon_table = {
        "A": 4,
        "R": 6,
        "D": 2,
        "N": 2,
        "C": 2,
        "E": 2,
        "Q": 2,
        "G": 4,
        "H": 2,
        "I": 3,
        "L": 6,
        "K": 2,
        "M": 1,
        "F": 2,
        "P": 4,
        "S": 6,
        "T": 4,
        "W": 1,
        "Y": 2,
        "V": 4,
        }
    total = 3  # start at 3 because of stop codons
    for i in range(len(seq)):
        total *= amino_codon_table[seq[i]]
    return total % 1000000


def has_motif(dna, sub):
    """
    Check if dna sequence contains subsequence

    Parameters
    ----------
    dna : str
        Input sequence of nucelotides

    Returns
    -------
    bool
        True if subsequence is in sequence
    """
    for i in range(len(dna)-len(sub)+1):
        if dna[i:i+len(sub)] == sub:
            return True
    return False


# TODO
# could make array global instead of passing
def check_motifs(dna_array, substring):
    """
    Check if substring is in all dna seqs

    Parameters
    ----------
    dna_array : list (of strings)
        Reference set of sequences
    substring : string
        substring to check

    Returns
    -------
    substring : list
         Only returns the substring if present in all dna seqs
    """
    glob_match = True
    for dna in dna_array:
        local_match = has_motif(dna, substring)
        if local_match:
            pass
        else:
            glob_match = False
        if local_match is False:
            break
    if glob_match is True:
            return substring


# ALGORITHM
# start with loop with shortest length
# check every other seq for full match
# break if not match in seq
# repeat with all substrings in (shortest_string - 1)
# would it be quicker to loop starting from the smallest?
# probably depends on the data set.  try it on rosalind
def longest_common_shared_motif(dna_array):
    """
    Determines the longest common shared subsequence in a list of sequences

    Parameters
    ----------
    dna_array : list (of strings)
        Input list of dna sequences

    Returns
    -------
    sub : str
         Longest common subsequence
    """
    shortest_dna = dna_array[0]
    for i in range(len(dna_array)):
        if len(shortest_dna) > len(dna_array[i]):
            shortest_dna = dna_array[i]
    len_shortest = len(shortest_dna)
    for n in reversed(range(len_shortest)):
        for j in range(len_shortest-n):
            sub = check_motifs(dna_array, shortest_dna[j:j+n+1])
            if sub:
                return sub


# I dont think this will work if there is more than one substring match
# because the loop will go wonky after the splice.
# fix by appending good dna to a diff string
def splice(dna_array):
    """
    Takes a seq and splices out all given substrings
    seq is then transcribed and translated to return protein

    Parameters
    ----------
    dna_array : list (of strings)
        First seq is main sequences, rest are subseqs

    Returns
    -------
    protein : str
        output sequence
    """
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


def random_string(seq, probs):
    """
    Calculates probability that a string could be randomly
    generated at a given GC percentage

    Parameters
    ----------
    seq : str
        Input sequence of nucelotides
    probs : list (of floats)
        gc percentage to compare
    Returns
    -------
    odds_of_string:
         Logaritm of probability of randomly constructing this string
    """
    len_probs = len(probs)
    odds_of_string = [0]*len_probs
    gc = calculate_gc(seq)
    for i in range(len_probs):
        pg = math.log10(probs[i]/2)
        pt = math.log10((1-probs[i])/2)
        for j in seq:
            if j == 'A' or j == 'T':
                odds_of_string[i] += pt
            else:
                odds_of_string[i] += pg
    return odds_of_string


# should rewrite the motif search using this table
def kmp_fail(seq):
    """
    Calculate failure array for KMP search function
    ref wikipedia entry on knuth morris pratt

    Parameters
    ----------
    seq : str
        Input sequence of nucelotides

    Returns
    -------
    fail_array : list (of ints)
         KMP failure array
    """
    fail_array = [0] * len(seq)
    streak = 0
    ind = 1
    while ind < len(seq):
        if seq[ind] == seq[streak]:
            streak += 1
            fail_array[ind] = streak
            ind += 1
        elif streak > 0:
            streak = fail_array[streak - 1]
        else:
            fail_array[ind] = streak
            ind += 1
    return fail_array


def find_met(seq):
    """
    Find index of all start codons in a sequence

    Parameters
    ----------
    seq : str
        Input sequence of nucelotides

    Returns
    -------
    start_locations : list (of ints)
        Index of all Met
    """
    start_locations = []
    for i in range(len(seq)-2):
        if seq[i] == 'A' and seq[i+1] == 'U' and seq[i+2] == 'G':
            start_locations.append(i)
    return start_locations


def translate_from_mets(seq, protein_array):
    """
    Translates sequence into proteins based locations of met
    Only stores unique proteins

    Parameters
    ----------
    seq : str
        Input sequence of nucelotides
    protein_array : list (of str)
        contains proteins already translated

    Returns
    -------
    start_locations : list (of ints)
        Index of all Met
    """
    mets = find_met(seq)
    for i in range(len(mets)):
        protein = translate(seq[mets[i]:])
        if protein and protein not in protein_array:
            protein_array.append(protein)
    return protein_array


def open_reading_frame(seq):
    """
    Figure out all possible proteins from a given seq
    Need to read seq both ways to find all start codons
    Only translate if it also has stop codon

    Parameters
    ----------
    seq : str
        Input sequence of nucelotides

    Returns
    -------
    protein_array : list (of strings)
         All possible protein seqs
    """
    seqA = to_rna_sense(seq)
    seqB = rev_comp(seq)
    protein_array = []
    protein_array = translate_from_mets(seqA, protein_array)
    protein_array = translate_from_mets(seqB, protein_array)
    return protein_array


# Recursion woooo
def enum_lex(n, alphabet=["T", "A", "G", "C"]):
    """
    Returns all possible words of length n that can be made from alphabet
    recursive algorithm to return words in lexographic order

    Parameters
    ----------
    n : int
        length of words to form
    alphabet : list
        set of letters to use

    Returns
    -------
    word_list : list (of strings)
         All possible words
    """
    if n == 1:
        return alphabet
    else:
        previous_output = enum_lex(n-1, alphabet)
        word_list = []
        for letter in alphabet:
            for i in range(len(previous_output)):
                word_list.append(letter+previous_output[i])
        return word_list


def trans_ratio(s, t):
    """
    Calculates transition/transversion ratio between two dna seqs

    Parameters
    ----------
    s,t : str
        input seqs to compare

    Returns
    -------
    transitions/transversions : float
         ratio of transitions to transversions
    """
    transitions, transversions = 0.0, 0.0
    for i in range(len(t)):
        if s[i] != t[i]:
            print "not match enter count loop"
            if s[i] == "G" and t[i] == "A" or s[i] == "A" and t[i] == "G":
                print "G <-> A transition"
                transitions += 1
            elif s[i] == "C" and t[i] == "T" or s[i] == "T" and t[i] == "C":
                print "C <-> T transition"
                transitions += 1
            else:
                print "transversion"
                transversions += 1
    return transitions/transversions


def spliced_motif(s, t):
    """
    Finds collection of indices of s in which the symbols of t are subseq
    not necessarily continuous

    Parameters
    ----------
    s : str
        input main sequence
    t : str
        subseq to locate

    Returns
    -------
    matches : list (of ints)
        indices of s that make up t
    """
    i, j = 0, 0
    while i in range(len(s) - len(t) - 1):
        matches = []
        while j <= len(t) - 1:
            if s[i] == t[j]:
                matches.append(i + 1)
                j += 1
                i += 1
            else:
                i += 1
            if j == len(t):
                return matches


# takes in array of lengths and original sequence
# finds index of longest seq with last value less than current value
# ie candidates for new longest seq (if there is one)
def find_longest_sub(len_seqs, sequence, i, sign="dec"):
    max_ind = None
    max_val = 1
    for j in range(i):
        if sign == "dec":
            if sequence[j] > sequence[i] and len_seqs[j] >= max_val:
                max_val = len_seqs[j]
                max_ind = j
        elif sign == "inc":
            if sequence[j] < sequence[i] and len_seqs[j] >= max_val:
                max_val = len_seqs[j]
                max_ind = j
    return max_ind


# takes seq, locate longest possible decreasing(or increasing) subseq
# ref wikipedia
def longest_subseq(sequence, sign="dec"):
    N = len(sequence)
    long_seq = [[]] * N
    len_sequence = [0] * N
    for i in range(N):
        if i == 0:
            long_seq[0] = str(sequence[0])
            len_sequence[0] = 1
        else:
            ind = find_longest_sub(len_sequence, sequence, i, sign)
            if ind is not None:
                long_seq[i] = long_seq[ind] + ' ' + str(sequence[i])
                len_sequence[i] = len_sequence[ind] + 1
            else:
                long_seq[i] = str(sequence[i])
                len_sequence[i] = 1
    return long_seq[len_sequence.index(max(len_sequence))]

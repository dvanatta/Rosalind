# library of simple functions for bioinformatics analysis DKV 9/2014
# this library should focus on functions which take dna string as input
#TODO assert statements on input and output and/or duck typing
#good comments
#use each rosalind problem as a unit test case for these functions


def count(DNA):
#input DNA string, returns count of of each nucleic acid
    A, T, C, G = 0, 0, 0, 0
    for nuc in DNA:
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


def to_dna(dna):
#input dna returns reverse complement DNA
    print "Deprecated, use rev_comp instead"
    dna_complement = ''
    for nuc in dna:
        dna_complement += complement_nuc(nuc)
    return dna_complement.reverse()


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



# library of functions to parse various rosalind files
import numpy
import urllib2


def parse_txt(filename):
    """input: name of file containing one dna seq per line
    returns: 1d array of strings, or just string if len(1)"""
    dna_list = []
    for line in open(filename):
        dna_list.append(line.rstrip())
    if len(dna_list) == 1:
        dna_list = dna_list[0]
    return dna_list


def parse_fasta(filename):
    """input: name of file containing seqs in fasta format
    returns: 2xN array of [label, seq]"""
    dataset = []
    row = 0
    store = ''
    for line in open(filename):
        line = line.rstrip()
        if line[0] == '>':
            line = line[1:len(line)]
            if store:
                dataset[row][1] = store
                store = ''
                row += 1
            dataset.append([line, 0])
        else:
            store += line
    dataset[row][1] = store
    return dataset


def parse_rosalind(filename):
    """ Support old wrapper scripts """
    print "parse_rosalind should be called parse_fasta"
    return parse_fasta(filename)


def seq_from_url(url):
    """input: url of unitpro access code
    returns: sequence - assumes one seq per url"""
    seq = ''
    data = urllib2.urlopen(url)
    for line in data:
        if line[0] == '>':
            pass
        else:
            seq += line.rstrip()
    return seq


def rosa_from_txt(filename, store_backup=False):
    """input: text filename with 1xN list of uniprot access codes
    returns: 2xN array of [[code, seq],[...] """
    names = parse_txt(filename)
    output_array = []
    savefile = open(filename+'.backupseqs', 'w')
    for code in names:
        output_array.append(
            [code.rstrip(), seq_from_url(
                'http://www.uniprot.org/uniprot/'+code+'.fasta')])
        if store_backup:
            savefile.write(code + '\n')
            savefile.write(seq_from_url(
                'http://www.uniprot.org/uniprot/' + code + '.fasta') + '\n')
    savefile.close()
    return output_array

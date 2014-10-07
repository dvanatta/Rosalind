# library of input parsers.  will probably end up with just fasta?
# if there aren't going to be other parser types I can just roll these two into a smart parser
import numpy
import urllib2

def parse_txt(filename):
#returns 1d array of dna strings, or just string if len(1)
    dna_list = []
    for line in open(filename):
        dna_list.append(line.rstrip())
    if len(dna_list) == 1:
        dna_list = dna_list[0]
    return dna_list

def parse_fasta(filename):
#parse fasta format into 2xN array of keys values (because dictionars are slower?) 
    dataset = []
    row = 0
    store =''
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

#deprecated use parse_fasta
def parse_rosalind(filename):
    print "parse_rosalind should be called parse_fasta"
    return parse_fasta(filename)


def seq_from_url(url):
    #given url, return sequence assume one seq per url
    seq = ''
    data = urllib2.urlopen(url)
    for line in data:
        if line[0] == '>':
            pass
        else:
            seq += line.rstrip()
    return seq 

def rosa_from_txt(filename, store_backup = False):
    #input text file with 1xN list of uniprot access codes, returns 2xN with [[code, seq],[...]
    names = parse_txt(filename)
    output_array = []
    savefile = open(filename+'.backupseqs', 'w')
    for code in names:
        output_array.append([code.rstrip(), seq_from_url('http://www.uniprot.org/uniprot/'+code+'.fasta')])
        if store_backup:
            savefile.write(code+'\n')
            savefile.write(seq_from_url('http://www.uniprot.org/uniprot/'+code+
'.fasta')+'\n')
    savefile.close()
    return output_array

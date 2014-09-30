# library of input parsers.  will probably end up with just fasta?

def parse_txt(filename):
#returns 1d array of dna strings, or just string if len(1)
    dna_list = []
    for line in open(filename):
        dna_list.append(line.rstrip())
    if len(dna_list) == 1:
        dna_list = dna_list[0]
    return dna_list

def parse_rosalind(filename):
#parse rosalind format into 2xN array of keys values (because dictionars are slower?) 
    dataset = []
    row = 0
    store =''
    for line in open(filename):
        line = line.rstrip()
        if line[0] == '>':
            if store:
                dataset[row][1] = store
                store = ''
                row += 1
            dataset.append([line, 0])
        else:
            store += line
    dataset[row][1] = store
    return dataset


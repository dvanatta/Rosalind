# library of input parsers.  will probably end up with just fasta?

def parse_rosalind(filename):
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


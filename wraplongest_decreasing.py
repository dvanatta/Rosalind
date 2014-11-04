import parser

sequence = parser.parse_numbers("rosalind_lgis.txt")[1]
#sequence = parser.parse_numbers("ex21.txt")[1]
#sequence = ["5","1","4","2","3"]
#sequence = ["0", "8", "4", "12", "2", "10", "6", "14", "1", "9", "5", "13", "3", "11", "7", "15"] 
#sequence = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5,13, 3, 11, 7,15] 
N = len(sequence)

def find_longest_dec(len_seqs, sequence, i):
    max_ind = None
    max_val = 1
    for j in range(i):
        if sequence[j] > sequence[i] and len_seqs[j] >= max_val:
            max_val = len_seqs[j]
            max_ind = j
    return max_ind
def find_longest_inc(len_seqs, sequence, i):
    max_ind = None
    max_val = 1
    for j in range(i):
        if sequence[j] < sequence[i] and len_seqs[j] >= max_val:
            max_val = len_seqs[j]
            max_ind = j
    return max_ind
        
        



#takes in array of lens and original sequence, finds index of longest seq with last value less than current value
def longest_decreasing_subseq(sequence):
    longest_sequence = [[]]*N
    len_sequence=[0]*N
    for i in range(N):
        if i == 0:
            longest_sequence[0] = str(sequence[0])
            len_sequence[0] = 1 
        else:
                    ind = find_longest_dec(len_sequence, sequence, i)
                    if ind != None:
                        longest_sequence[i] = longest_sequence[ind]+ ' ' + str(sequence[i])
                        len_sequence[i] = len_sequence[ind] + 1 
                    else:
                        longest_sequence[i] = str(sequence[i])
                        len_sequence[i] = 1 
    print longest_sequence[len_sequence.index(max(len_sequence))]
def longest_increasing_subseq(sequence):
    longest_sequence = [[]]*N
    len_sequence=[0]*N
    for i in range(N):
        if i == 0:
            longest_sequence[0] = str(sequence[0])
            len_sequence[0] = 1 
        else:
                    ind = find_longest_inc(len_sequence, sequence, i)
                    if ind != None:
                        longest_sequence[i] = longest_sequence[ind]+ ' ' + str(sequence[i])
                        len_sequence[i] = len_sequence[ind] + 1 
                    else:
                        longest_sequence[i] = str(sequence[i])
                        len_sequence[i] = 1 
    print longest_sequence[len_sequence.index(max(len_sequence))]

longest_increasing_subseq(sequence, "inc")
longest_decreasing_subseq(sequence, "dec")

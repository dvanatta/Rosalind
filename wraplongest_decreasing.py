import parser

#sequence = parser.parse_numbers("rosalind_lgis.txt")[1]
#sequence = parser.parse_numbers("ex21.txt")[1]
#sequence = ["5","1","4","2","3"]
#sequence = ["0", "8", "4", "12", "2", "10", "6", "14", "1", "9", "5", "13", "3", "11", "7", "15"] 
sequence = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5,13, 3, 11, 7,15] 
N = len(sequence)

def find_longest(len_seqs, sequence, i):
    print "called find longest, i=", i
    max_ind = None
    max_val = 1
    for j in range(i):
        print "seqj seqi", sequence[j], sequence[i]
        if sequence[j] > sequence[i] and len_seqs[j] >= max_val:
            max_val = len_seqs[j]
            max_ind = j
            print "seqi,seqj, len_seqs, max_val", sequence[i],sequence[j],len_seqs,max_val,max_ind
#    if max_ind != None:
#    print max_ind
    return max_ind
        
        



#takes in array of lens and original sequence, finds index of longest seq with last value less than current value
def longest_increasing_subseq(sequence):
    longest_sequence = [[]]*N
    len_sequence=[0]*N
    for i in range(N):
        print "i=",i
        if i == 0:
            longest_sequence[0] = str(sequence[0])
            len_sequence[0] = 1 
        else:
#            for j in range(N):
#                    print "j=",j
                    ind = find_longest(len_sequence, sequence, i)
                    print "ind =", ind
#                if sequence[j] < sequence[i] :
#                    print "i,j", i,j
                    print sequence, longest_sequence, len_sequence
                    if ind != None:
                        print longest_sequence[i], longest_sequence[ind], sequence[i]
                        longest_sequence[i] = longest_sequence[ind]+ ' ' + str(sequence[i])
                        len_sequence[i] = len_sequence[ind] + 1 
                        print "here?", sequence, longest_sequence, len_sequence
#                    break 
                    else:
#        if longest_sequence[i] == []:
                        longest_sequence[i] = str(sequence[i])
                        len_sequence[i] = 1 
                        print "lonegest seq is now", longest_sequence
            #find all in longest_seq with longest_seq[
    print max(len_sequence)
    print longest_sequence[len_sequence.index(max(len_sequence))]

longest_increasing_subseq(sequence)

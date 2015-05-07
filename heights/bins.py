import dna_parser
import math

data = dna_parser.parse_txt('rosalind_bins.txt')
n = int(data[0])
m = int(data[1])

A = map(int, data[2].split())
k = map(int, data[3].split())


def divcon(array, key, length, start_value):
#    print array, key, length, start_value
    if array == []:
        print "no match"
        return -1
    elif key == array[length/2]:
        print "winning", start_value, length/2
        return start_value + length/2 
    elif key < array[length/2]:
        print "key < value", key, array[length/2]
        return divcon(array[0:length/2], key, length/2, start_value)
    else: #key > array[length/2]:
        print "key > value", key, array[length/2]
        print "length, length/2", length, length/2
        if length % 2 != 0:
            return divcon(array[length/2+1:length], key, length/2 , length/2 + 1 + start_value)
        else:
            return divcon(array[length/2:length], key, length/2 , length/2  + start_value)

output = []
for i in k:
    output.append(divcon(A,i,n,1))    
  
print " ".join(map(str,output))


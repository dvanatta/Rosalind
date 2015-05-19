import dna_parser

data = dna_parser.parse_txt('rosalind_2sum.txt')
k = int(data[0].split()[0])
n = int(data[0].split()[1])
def twosum(A):
    for i in range(n):
        for j in range(i + 1, n):
            if A[j] == -A[i]:
                return [i + 1, j + 1]
    return [-1]


for i in range(1, k + 1):
    print " ".join(map(str,twosum(map(int,data[i].split()))))

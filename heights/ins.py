import dna_parser


data = dna_parser.parse_txt('rosalind_ins.txt')
A = map(int, data[1].split())
#A = [6, 10, 4, 5, 1, 2]


def insertion_sort(A, counter):
    for i in range(1,len(A)):
        while i >= 1 and A[i] < A[i-1]:
            temp = A[i]
            A[i] = A[i-1]
            A[i-1] = temp
            i -= 1
            counter += 1
    return counter


print insertion_sort(A, 0)

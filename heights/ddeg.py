#data=open('rosalind_ddeg.txt').read().split('\n')
data = map(int,open('rosalind_ddeg.txt').read().split())
print data
num_vert = data[0]
num_edges = data[1]

A = []
for i in range(1,len(data)/2):
    A.append([data[2*i],data[2*i+1]])

linked_list = []
for i in range(num_vert):
    linked_list.append([])
    for j in A:
        if j[0] == i+1:
            linked_list[i].append(j[1])
        elif j[1] == i+1:
            linked_list[i].append(j[0])
            
print linked_list
D = [0]*num_vert
for i in range(num_vert):
    for j in linked_list[i]:
        D[i] += len(linked_list[j-1])

print " ".join(map(str,D))
        

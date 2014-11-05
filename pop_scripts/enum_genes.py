import itertools
N = 2
int_array = range(-N, N + 1)
int_array.remove(0)
output = list(itertools.permutations(int_array, N))
unique_output = []
for i in range(len(output)):
    pos_list = [abs(j) for j in output[i]]
    if len(pos_list) == len(set(pos_list)):
        unique_output.append(output[i])
print len(unique_output)
for i in range(len(unique_output)):
    print " ".join(str(num) for num in unique_output[i])

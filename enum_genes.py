import itertools
N = 2
int_array = range(-N,N+1)
int_array.remove(0)
output = list(itertools.permutations(int_array,N))
unique_output = []
for i in range(len(output)):
    pos_list = [abs(j) for j in output[i]]
    if len(pos_list) == len(set(pos_list)):
        unique_output.append(output[i])
print len(unique_output)        
for i in range(len(unique_output)):
    print " ".join(str(num) for num in unique_output[i])





#    print output[i][0], output[i][1], output[i][2], output[i][3], output[i][4], output[i][5], output[i][6]


#print ' '.join(str(i) for i in output)






#def enum_gene_orders(elements):
#    print elements, len(elements)
#    if len(elements) == 1:
#        print "here"
#        yield elements
#    else:
#        for perm in all_perms[elements[1:]]:
#            for i in range(len(elements)):
#                print str(perm[:1] + elements[0:1] + perm[i:])
#                yield perm[:1] + elements[0:1] + perm[i:]

#enum_gene_orders([1,2,3])

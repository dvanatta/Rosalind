import parser

data = parser.parse_fasta("rosalind_tran.txt")

s = data[0][1]
t = data[1][1]

print s
print t
transitions, transversions = 0.0, 0.0

for i in range(len(t)):
    print s[i], t[i]
    if s[i] != t[i]:
        print "not match enter count loop"
        if s[i] == "G" and t[i] == "A" or s[i] == "A" and t[i] == "G" or s[i] == "C" and t[i] == "T" or s[i] == "T" and t[i] == "C":
            print "transition"
            transitions += 1
        else:
            print "transversion"
            transversions +=1
print transitions/transversions



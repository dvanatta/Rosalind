# figure out how to deal with the global vairable when you roll into dna.py
# actually this probably doesn't go in dna.py
# k m n individuals
# count dominant allele

pairs = []


def mate(k, m, n):
    individual = "k" * k + "m" * m + "n" * n
    for i in range(len(individual) - 1):
        pairs.append(individual[0] + individual[i + 1])
    if individual:
        if individual[0] == 'k':
            mate(k - 1, m, n)
        if individual[0] == 'm':
            mate(k, m - 1, n)
        if individual[0] == 'n':
            mate(k, m, n - 1)
    else:
        print pairs
        return pairs


def sum(pairs):
    count = 0.0
    for i in pairs:
        if i[0] == 'k' or i[1] == 'k':
            count += 1
        elif i[0] == 'm' and i[1] == 'm':
            count += .75
        elif i[0] == 'm' and i[1] == 'n' or i[0] == 'n' and i[1] == 'm':
            count += .5
        elif i[0] == 'n' and i[1] == 'n':
            count += 0
        else:
            print i
    return count / len(pairs)
mate(20, 28, 23)

print sum(pairs)

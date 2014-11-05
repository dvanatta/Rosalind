n, m = 81, 19
gens = [1, 1]


def fib(i, j):
    count = 2
    while (count < i):
        if (count < j):
            gens.append(gens[-2] + gens[-1])
        elif (count == j or count == j+1):
            gens.append((gens[-2] + gens[-1]) - 1)
        else:
            gens.append((gens[-2] + gens[-1]) - (gens[-(j+1)]))
        count += 1
    return (gens[-1])


print fib(n, m)

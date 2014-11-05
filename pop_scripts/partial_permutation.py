import math
n = 91
k = 10


def binomial_coefficient(n, k):
    if k > n / 2:
        k = n - k
    result = 1.0
    for i in range(1, k + 1):
        result *= ((n - (k - i)) / float(i))
    return result
print (math.factorial(n) / math.factorial(n-k)) % 1000000

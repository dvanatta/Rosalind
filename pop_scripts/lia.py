import math

def binomial(n,k):
    Prob = math.factorial(n)/math.factorial(k)/math.factorial(n-k)
    return Prob
def main(k,N):
    prob = 0
    p = .25
    q = 1 - p
    total = 2**k
    for i in range(N, total+1):
        prob += binomial(total,i)*(p**i)*(q**(total-i))
    return prob


print main(6,18)


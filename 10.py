
def sum(size):
    sumPrimes, sieve = 0, [True] * size
    for x in range(2, size):
        if sieve[x]:
            sumPrimes += x
            for i in range(2*x, size, x):
                sieve[i] = False
    return sumPrimes

print sum(2000000)


def countPrimes(self, n: int) -> int:
    if (n <= 1):
        return 0
    isPrime = [True]*(n)
    i = 2
    while (i*i < n):
        if isPrime[i]:
            for j in range(i*i, n, i):
                isPrime[j] = False
        i += 1
    return isPrime.count(True)-2

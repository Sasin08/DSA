def largestPrimeFactor(self, n):
    s = int(n**0.5)
    while n % 2 == 0:
        lp = 2
        n /= 2
    while n % 3 == 0:
        lp = 3
        n /= 3
    for i in range(5, s+1):
        if n == 1:
            break
        else:
            while n % i == 0:
                lp = i
                n /= i
    if n != 1:
        lp = n
    return int(lp)

def commonFactors(self, a: int, b: int) -> int:
    m = min(a, b)
    res = 1
    for i in range(2, m+1):
        if a % i == 0 and b % i == 0:
            res += 1
    return res

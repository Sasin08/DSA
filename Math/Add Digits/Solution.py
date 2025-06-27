def addDigits(self, num: int) -> int:
    s = str(num)
    sum = num
    while len(s) != 1:
        isum = 0
        for i in s:
            isum += int(i)
        s = str(isum)
        sum = isum
    return sum

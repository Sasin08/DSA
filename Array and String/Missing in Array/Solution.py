def missingNum(self, arr):
    s = 0
    for i in range(1, len(arr)+2):
        s += i
    return s-sum(arr)

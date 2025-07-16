def findEquilibrium(self, arr):
    s = sum(arr)
    subs = arr[0]
    for i in range(1, len(arr)):
        if (subs == s-subs-arr[i]):
            return i
        subs += arr[i]
    return -1

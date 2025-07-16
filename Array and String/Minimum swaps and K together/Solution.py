def minSwap(self, arr, k):
    n = len(arr)
    count = 0
    for i in arr:
        if i <= k:
            count += 1
    h = sum(1 for i in arr[:count] if i > k)
    res = h
    for j in range(count, n):
        if arr[j-count] > k:
            h -= 1
        if arr[j] > k:
            h += 1
        res = min(res, h)
    return res

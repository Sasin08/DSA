def sortInWave(self, arr):
    n = len(arr)
    for i in range(1, n, 2):
        arr[i], arr[i-1] = arr[i-1], arr[i]
    return arr

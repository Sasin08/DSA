def findDuplicates(self, arr):
    l = []
    arr = sorted(arr)
    for i in range(len(arr)-1):
        if len(l) != 0:
            if arr[i] == arr[i+1] and arr[i] != last:
                l.append(arr[i])
                last = arr[i]
                i += 2
        else:
            if arr[i] == arr[i+1]:
                l.append(arr[i])
                last = arr[i]
                i += 2
    return l

def aggressiveCows(self, stalls, k):
    def is_possible(d):
        count = 1
        last = stalls[0]
        for i in range(1, len(stalls)):
            if stalls[i]-last >= d:
                count += 1
                last = stalls[i]
                if count == k:
                    return True
        return False
    stalls.sort()
    l = 1
    h = stalls[-1]-stalls[0]
    res = 0
    while l <= h:
        mid = (l+h)//2
        if is_possible(mid):
            res = mid
            l = mid+1
        else:
            h = mid-1
    return res

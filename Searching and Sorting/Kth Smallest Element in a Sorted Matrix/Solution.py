def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
    m = len(matrix)
    n = len(matrix[0])
    lo = matrix[0][0]
    hi = matrix[-1][-1]

    def countele(mid):
        count = 0
        r = m-1
        c = 0
        while r >= 0 and c < m:
            if matrix[r][c] <= mid:
                count += r+1
                c += 1
            else:
                r -= 1
        return count
    while lo < hi:
        mid = (lo+hi)//2
        co = countele(mid)
        if co >= k:
            hi = mid
        else:
            lo = mid+1
    return lo

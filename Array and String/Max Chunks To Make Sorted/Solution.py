def maxChunksToSorted(self, arr: List[int]) -> int:
    high = 0
    chunks = 0
    for i in range(len(arr)):
        high = max(arr[i], high)
        if i == high:
            chunks += 1
    return chunks

def maxSubarraySize(arr, k):
    n = len(arr)
    low = 1
    high = n
    while low <= high:
        mid = low + (high - low) // 2
        sum_val = 0
        maxSum = -float('inf')
        for i in range(n):
            sum_val += arr[i]
            if i >= mid:
                sum_val -= arr[i - mid]
            if i >= mid - 1:
                maxSum = max(maxSum, sum_val)
        if maxSum <= k:
            low = mid + 1
        else:
            high = mid - 1
    if high == 0:
        return -1
    return high

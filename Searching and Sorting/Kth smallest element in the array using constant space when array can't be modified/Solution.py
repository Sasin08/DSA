def kthSmallest(arr, k, n) : 
    low = min(arr); 
    high = max(arr); 
    while (low <= high) :
        mid = low + (high - low) // 2; 
        countless = 0; countequal = 0; 
        for i in range(n) :
            if (arr[i] < mid) :
                countless += 1; 
            elif (arr[i] == mid) :
                countequal += 1; 
        if (countless < k and (countless + countequal) >= k) :
            return mid; 
        elif (countless >= k) :
            high = mid - 1; 
        elif (countless < k and countless + countequal < k) :
            low = mid + 1;

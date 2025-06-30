def searchRange(self, nums: List[int], target: int) -> List[int]:
    if len(nums) == 0:
        return [-1, -1]
    elif len(nums) == 1:
        if nums[0] == target:
            return [0, 0]
        else:
            return [-1, -1]
    else:
        l = 0
        r = len(nums)-1
        while l <= r:
            mid = (l+r)//2
            if nums[mid] == target:
                if nums[mid+1] == target:
                    return [mid, mid+1]
                elif nums[mid-1] == target:
                    return [mid-1, mid]
            elif nums[mid] > target:
                r = mid-1
            else:
                l = mid+1
        return [-1, -1]

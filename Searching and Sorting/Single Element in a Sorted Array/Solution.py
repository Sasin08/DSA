def singleNonDuplicate(self, nums: List[int]) -> int:
    i = 0
    while i < len(nums)-1:
        if nums[i] == nums[i+1]:
            i += 2
        else:
            return nums[i]
    return nums[-1]

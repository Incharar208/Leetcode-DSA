class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        if k > len(nums):
            k = k % len(nums)
        k1 = len(nums) - k
        i = 0
        j = k1 - 1
        n = len(nums)
        while i <= j:
            nums[i],nums[j] = nums[j],nums[i]
            i = i + 1
            j = j - 1

        i = k1
        j = n - 1  
        while i <= j:
            nums[i],nums[j] = nums[j],nums[i]
            i = i + 1
            j = j - 1
        i= 0
        j = n-1
        while i <= j:
            nums[i],nums[j] = nums[j],nums[i]
            i = i + 1
            j = j - 1

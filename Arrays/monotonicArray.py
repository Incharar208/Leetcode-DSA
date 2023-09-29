# time complexity : O(n)
# space complexity : O(1)

class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        i = 0
        j = len(nums) - 1
        if nums[i] > nums[j]:
            for i in range(len(nums)-1):
                if nums[i] == nums[i+1] or nums[i] > nums[i+1]:
                    pass
                else:
                    return False
        else:
            for i in range(len(nums)-1):
                if nums[i] == nums[i+1] or nums[i] < nums[i+1]:
                    pass
                else:
                    return False
        return True

class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        increasing = True
        decreasing = True
        for i in range(len(nums)-1):
            if nums[i] < nums[i+1]:
                decreasing = False

        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                increasing = False

        return increasing or decreasing

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

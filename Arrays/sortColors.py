class Solution:
    def sortColors(self, nums: List[int]) -> None:
        countOf0 = 0
        countOf1 = 0
        countOf2 = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                countOf0 = countOf0 + 1
            if nums[i] == 1:
                countOf1 = countOf1 + 1
            if nums[i] == 2:
                countOf2 = countOf2 + 1  

        for i in range(0,countOf0):
            nums[i] = 0
        for i in range(countOf0,countOf0 + countOf1):
            nums[i] = 1
        for i in range(countOf0 + countOf1,countOf0 + countOf2 + countOf1):
            nums[i] = 2  

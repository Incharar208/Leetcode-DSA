class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        n=len(nums)
        j=0
        # first arranging all the non zero numbers
        for i in range(n):
            if nums[i]!=0:
                nums[j]=nums[i]
                j=j+1
        # adding zeroes  
        while j<n:
           nums[j]=0
           j=j+1

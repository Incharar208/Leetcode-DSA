class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maximum=-999999
        Sum=0
        for i in range(len(nums)):
            Sum=Sum+nums[i]
            maximum=max(maximum,Sum)
            if Sum<0:
                Sum=0

        return maximum            



class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        firstMax = max(nums)
        nums.remove(firstMax)
        secondMax = max(nums)
        outputSum = (firstMax - 1) * (secondMax - 1)
        return outputSum
        

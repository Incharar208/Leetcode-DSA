class Solution:
    def minDifference(self, nums: List[int]) -> int:
        # handling the inital condition first, 
        if len(nums) <= 4:
            return 0
        # using a heap inorder to choose the smallest 4 values 
        # and largest 4 values
        # and finding out the minimum difference between these
        # considered 4 values
        value = float("inf") # considering the value to the the highest possible number
        maxValues = sorted(heapq.nlargest(4, nums))
        minValues = sorted(heapq.nsmallest(4, nums))
        for i in range(4):
            value = min(value, (maxValues[i] - minValues[i]))
        return value

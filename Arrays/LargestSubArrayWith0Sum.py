#GFG QUESTION
from collections import defaultdict

class Solution:
    def maxLen(self, n, arr):
        hashMap = defaultdict(int)
      '''
       we keep a value for 0 as -1
       for cases like 0, 1, 2 : the solution will be 1 
       '''
        hashMap[0] = -1
        
        runningSum = 0
        lengthValue = 0
        # keeping track of both indexes and the value in the array
        for i, value in enumerate(arr):
            runningSum = runningSum + value
            if runningSum not in hashMap:
                hashMap[runningSum] = i
            # we update the maximum value of the lengths
            else:
                lengthValue = max(lengthValue, i - hashMap[runningSum])
                
        return lengthValue

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        hashMap = defaultdict(int)
        #  initialising {0: -1}
        hashMap[0] = -1
        runningSum = 0
        lengthValue = 0 

        for i, value in enumerate(nums):
            if value == 0:
                runningSum = runningSum - 1
            if value == 1:
                runningSum = runningSum + 1

            if runningSum not in hashMap:
                hashMap[runningSum] = i
            else:
                lengthValue = max(lengthValue, i - hashMap[runningSum])

        return lengthValue

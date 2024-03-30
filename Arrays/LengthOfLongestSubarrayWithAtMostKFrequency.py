class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        hashMap = defaultdict(int)
        lengthOfSubArrays = 0
        i, j = 0, 0

        while j < len(nums):
            hashMap[nums[j]] = hashMap[nums[j]] + 1
            if hashMap[nums[j]] <= k:
                lengthOfSubArrays =max(lengthOfSubArrays, (j - i + 1)) 
            else:
                while hashMap[nums[j]] > k:
                    hashMap[nums[i]] = hashMap[nums[i]] - 1
                    i = i + 1
                lengthOfSubArrays = max(lengthOfSubArrays, (j - i + 1))

            j = j + 1    

        return lengthOfSubArrays

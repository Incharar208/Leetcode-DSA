class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        hashMap = defaultdict(int)

        for i in nums:
            hashMap[i] = hashMap[i] + 1
        
        for key, value in hashMap.items():
            if value != 1:
                return key

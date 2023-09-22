class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        hashMap = dict()
        indexList = []
        for i in range(n) :
            requiredValue = target - nums[i]
            if requiredValue in hashMap :
                indexList.append(i)
                indexList.append(hashMap[requiredValue])
            else :
                hashMap[nums[i]] = i

        return indexList          

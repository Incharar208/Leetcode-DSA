# approaches
# Brute force: for each element compare every othe elements sum
# Using hashMap
# it can be solved using two pointers also.



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

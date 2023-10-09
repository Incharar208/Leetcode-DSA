class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        resultList = []
        for i in range(len(nums)):
            if nums[i] == target:
                resultList.append(i)

        return resultList        

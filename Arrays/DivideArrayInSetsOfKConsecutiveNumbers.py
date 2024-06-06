class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        # if array length is not a mutliple of k, we return false
        if len(nums) % k != 0:
            return False

        nums.sort()
        arrayWithCount = Counter(nums)

        for i in nums:
            if not arrayWithCount[i]:
                continue
            arrayWithCount[i] = arrayWithCount[i] - 1
            for j in range(1,k):
                value = i + j
                if not arrayWithCount[value]:
                    return False
                arrayWithCount[value] = arrayWithCount[value] - 1

        return True

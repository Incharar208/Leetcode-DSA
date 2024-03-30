class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0

        count = 0
        product = 1
        i, j = 0, 0

        while j < len(nums):
            product = product * nums[j]
            if product < k:
                count = count + (j - i + 1)
            elif product >= k:
                while product >= k:
                    product = product // nums[i]
                    i = i + 1

                count = count + (j - i + 1)
            j = j + 1

        return count

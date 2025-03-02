class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hashMap = defaultdict(int)

        for i, num in enumerate(nums):
            if num in hashMap and i - hashMap[num] <= k:
                return True
            else:
                hashMap[num] = i

        return False

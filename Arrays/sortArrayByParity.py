# two pointers
#  time complexity : O(n)
# space complexity : O(1) - inplace solution
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        i = 0 #begining pointer
        j = len(nums) - 1 #ending pointer
        while i < j :
            if nums[i] % 2 == 0 :
                if nums[j] % 2 == 0 :
                    i = i + 1
                else :
                    i = i + 1
            else:
                if nums[j] % 2 == 0 :
                    nums[i] , nums[j] = nums[j] , nums[i]
                    i = i + 1
                    j = j - 1

                else :
                    j = j - 1

        return nums                


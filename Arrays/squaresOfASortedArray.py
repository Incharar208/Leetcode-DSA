# time complexity : O(n logn )
# space complexity : O(1)

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)) :
            nums[i] = nums[i] ** 2

        nums.sort()

        return nums


# time complexity : O(n)
# space complexity : O(n)
# two pointer approach : finding the maximum value and appending the maximum value to a list and the reversing the list to get ascending order
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        answerList = []
        i = 0 #beginning pointer
        j = len(nums) - 1 #ending pointer

        while i <= j : #until the indices cross
            if (nums[i] ** 2) > (nums[j] ** 2) :
                answerList.append(nums[i]**2)
                i = i + 1
            else :
                answerList.append(nums[j]**2)    
                j = j - 1

        answerList = answerList[::-1]

        return answerList        

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        # solution that takes 
        # time complexity: O(n)
        # space complexity: O(1)

        # list to store the output
        answerList = []

        for i in nums:
            # let us compute the index value
            indexValue = abs(i) - 1
            # if index value is less than 0, duplicate is found and we insert to the answerList
            if nums[indexValue] < 0:
                answerList.append(abs(i))
            # if not, we will make the value negative so that it becomes a mark that its the first occurence
            else:
                nums[indexValue] = - nums[indexValue]

        return answerList

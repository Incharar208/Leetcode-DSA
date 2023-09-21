class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        low = 0
        high = n-1
        index1 = -1
        index2 = -1
        solutionList = []
        while low <= high :
            mid = int(low+(high-low)/2)
            if nums[mid] == target :
                index1 = mid
                high = mid-1
            elif nums[mid] < target :
                low = mid + 1
            else:
                high = mid - 1

        low = 0
        high = n-1   

        while low <= high :
            mid = int(low+(high-low)/2)
            if nums[mid] == target :
                index2 = mid
                low = mid + 1
            elif nums[mid] < target :
                low = mid + 1
            else:
                high = mid - 1
            
        solutionList.append(index1)
        solutionList.append(index2) 
        
        return solutionList
        

# GFG
class Solution:
    def isMaxHeap(self,arr,n):
        for i in range(n):
            leftChildValue = 2 * i + 1
            rightChildValue = 2 * i + 2
            if leftChildValue < n:
                if arr[leftChildValue] > arr[i]:
                    return 0
                    
            if rightChildValue < n:
                if arr[rightChildValue] > arr[i]:
                    return 0
                    
        return 1

# GFG QUESTION:

class Solution:
    def sort012(self,arr,n):
        countOf0 = 0
        countOf1 = 0
        countOf2 = 0
        
        for i in arr:
            if i == 0:
                countOf0 = countOf0 + 1
            if i == 1:
                countOf1 = countOf1 + 1
            if i == 2:
                countOf2 = countOf2 + 1
                
        for i in range(countOf0):
            arr[i] = 0
            
        for i in range(countOf0, countOf0 + countOf1):
            arr[i] = 1
            
        for i in range(countOf0 + countOf1 , n):
            arr[i] = 2

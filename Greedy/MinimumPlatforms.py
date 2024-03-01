# GFG QUESTION.

class Solution:    
    # Function to find the minimum number of platforms required at the
    # railway station such that no train waits.
    def minimumPlatform(self,n,arr,dep):
        # we need to ensure that the arrival and departure arrays are sorted.
        arr.sort()
        dep.sort()
        
        platForms = 1
        total = 1
        
        # using two pointers 
        i = 1 # for arrival array
        # we consider the first train to be arrived already
        j = 0
        # for checking the departure times
        
        while i < n and j < n:
            if arr[i] <= dep[j]:  # if a train arrives , even before a train has left the platform
                platForms = platForms + 1
                i = i + 1
                
            elif arr[i] > dep[j]:
                platForms = platForms - 1
                j = j + 1
                
            if platForms > total:
                total = platForms
                
        return total

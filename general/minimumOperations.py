# GFG Question

class Solution:
    def minOperation(self, n):
        count = 0
        while n>0:
            if n % 2 == 0:
                n = n / 2

            else:
                n = n - 1
            
            count = count + 1
        
        return count

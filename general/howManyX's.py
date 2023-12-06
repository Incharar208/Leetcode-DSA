# GFG QUESTION

class Solution:    
    def countX(self,L,R,X):
        count = 0
        for i in range(L+1,R):
            x = str(i)
            if x.count(str(X)) >= 1:
                n = x.count(str(X))
                count = count + n
            else:
                pass
            
        return count
            
        

#User function Template for python3
# GFG QUESTION

class Solution:
	def TotalWays(self, N):
	    if N == 1:
	        return 4
	    if N == 2:
	        return 9
	        
	    n1 = 2
	    n2 = 3
	    
	    for i in range(3,N+1):
	        n3 = (n1+n2) % 1000000007
	        n1 = n2
	        n2 = n3
	        
	    return (n3 ** 2) % 1000000007
	        

# GFG Question

class Solution:
    def solve(self, N, R):
        if R == 0:
            return 1
            
        if R == 1:
            return N
            
        if R % 2 == 0:
            value = self.solve(N, R / 2)
            return (value * value) % ((10**9)+7)
        else:
            return (N * self.solve(N, R-1)) % ((10**9)+7)
    
        
    def power(self, N, R):
        answer = self.solve(N, R)
        return (answer) 

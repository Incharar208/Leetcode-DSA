class Solution:
    def solve(self, count, size, s):
        if count == size:
            s.pop()
            return
            
        x = s.pop()
        self.solve(count + 1, size, s)
        s.append(x)

    def deleteMid(self, s, sizeOfStack):
        count = 1
        size = int(sizeOfStack / 2 + 1 )
        
        self.solve(count, size, s)

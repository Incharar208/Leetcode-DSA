class Solution:
    def solve(self, St):
        if not St:
            return
        x = St.pop() 
        self.solve(St)
        self.insertToBottom(St, x)

    def insertToBottom(self, St, x):
        if not St:
            St.append(x)  # append the first popped element, if stack is empty
            return 
        y = St.pop()  
        self.insertToBottom(St, x)
        St.append(y)
            
    def reverse(self,St): 
        self.solve(St)

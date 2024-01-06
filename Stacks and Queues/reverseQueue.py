class Solution:
    #Function to reverse the queue.
    def rev(self, q):
        # a stack
        stack = []
        
        while not q.empty():
            stack.append(q.get())
            
        while stack:
            q.put(stack.pop())
            
        return q

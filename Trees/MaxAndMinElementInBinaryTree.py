# GFG QUESTION.
'''
class Node:
    def __init__(self,val):
        self.data=val
        self.left=None
        self.right=None
'''
class Solution:
    def findMax(self,root):
        if root is None:
            return -1
        maximum = 0
        maximumLeft = root.data
        maximumRight = root.data
        rootLeft = root
        while rootLeft != None:
            maximumLeft = max(maximumLeft, rootLeft.data)
            rootLeft = rootLeft.left
        
        rootRight = root
        while rootRight != None:
            maximumRight = max(maximumRight, rootRight.data)
            rootRight = rootRight.right
            
        maximum = max(maximumLeft, maximumRight)
        return maximum
        
    def findMin(self,root):
        if root is None:
            return -1
        minimum = 0
        minimumLeft = root.data
        minimumRight = root.data
        rootLeft = root
        while rootLeft != None:
            minimumLeft = min(minimumLeft, rootLeft.data)
            rootLeft = rootLeft.left
        rootRight = root
        while rootRight != None:
            minimumRight = min(minimumRight, rootRight.data)
            rootRight = rootRight.right
            
        minimum = min(minimumLeft, minimumRight)
        return minimum

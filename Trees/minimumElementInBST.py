"""
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
"""

class Solution:
    #Function to find the minimum element in the given BST.
    def minValue(self, root):
        if root is None:
            return -1
          
        while root.left != None:
            root = root.left
            
        return root.data

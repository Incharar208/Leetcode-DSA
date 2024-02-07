# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, root):
        if root is None:
            return 0
        
        leftValue = self.helper(root.left)
        rightValue = self.helper(root.right)
        
        return 1 + max(leftValue, rightValue)

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        answer = self.helper(root)
        return answer

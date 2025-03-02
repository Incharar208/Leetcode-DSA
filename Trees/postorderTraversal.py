# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# RECURSIVE
class Solution:
    def postOrder(self,root,answerList):
        if root == None:
            return answerList
        else:
            self.postOrder(root.left, answerList)
            self.postOrder(root.right, answerList)
            answerList.append(root.val)

    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        answerList = []
        self.postOrder(root, answerList)

        return answerList
        

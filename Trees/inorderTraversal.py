# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# RECURSIVE
class Solution:
    def inOrder(self,root,answerList):
        if root == None:
            return
        else:
            self.inOrder(root.left, answerList)
            answerList.append(root.val)
            self.inOrder(root.right, answerList)



    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        answerList = []
        self.inOrder(root, answerList)

        return answerList

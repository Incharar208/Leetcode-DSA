class Solution:
    def helper(self, root, setForUse, level):
        if root is None:
            return 
        
        if root.left is None and root.right is None:
            setForUse.add(level)
        
        self.helper(root.left, setForUse, level + 1)
        self.helper(root.right, setForUse, level + 1)
        
        return len(setForUse) == 1
        
    def check(self, root):
        setForUse = set()
        answer = self.helper(root, setForUse, 0)
        return answer

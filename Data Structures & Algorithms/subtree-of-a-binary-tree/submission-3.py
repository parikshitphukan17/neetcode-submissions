# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def dfs(n1,n2):
            if not n1 or not n2:
                return not n1 and not n2
            if n1.val != n2.val:
                return False
            return dfs(n1.left,n2.left) and dfs(n1.right,n2.right)
        def check(node):
            if not node:
                return subRoot == None
            if dfs(node,subRoot):
                return True
            return check(node.left) or check(node.right)
        return check(root)

        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        equal = True
        def dfs(node):
            nonlocal equal
            if not node or not equal:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            if abs(left-right) >1:
                equal = False
                return 0
            return 1 + max(left,right)
        dfs(root)
        return equal
        
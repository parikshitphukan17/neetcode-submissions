# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.s = -1001
        def dfs(node):
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            self.s = max(self.s,node.val,node.val+left,node.val+right,node.val+left+right)
            return max(node.val,node.val+left,node.val+right)
        dfs(root)
        return self.s
        
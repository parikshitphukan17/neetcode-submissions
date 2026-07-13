# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = -1001
        def dfs(node):
            nonlocal res
            if not node:
                return -1001
            left = dfs(node.left)
            right = dfs(node.right)
            res = max(res,node.val,left+node.val,right+node.val,left+node.val+right)
            return max(left+node.val,node.val,node.val+right)
        dfs(root)
        return res
        

        
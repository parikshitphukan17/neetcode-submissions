# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.res = float("-inf")
        def dfs(node):
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            maxBranch = max(right+node.val,left+node.val,node.val)
            curTree = max(left+right+node.val,maxBranch)
            self.res = max(self.res,curTree)
            return maxBranch
        dfs(root)
        return self.res
        
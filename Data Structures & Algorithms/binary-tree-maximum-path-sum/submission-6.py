# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.res = -1001
        if not root:
            return 0
        
        def dfs(node):
            if not node:
                return -1001
            left = dfs(node.left)
            right = dfs(node.right)
            self.res = max(self.res,left+right+node.val,left+node.val,right+node.val,node.val)
            return max(node.val,node.val+left,node.val+right)
        dfs(root)
        return self.res
        

        
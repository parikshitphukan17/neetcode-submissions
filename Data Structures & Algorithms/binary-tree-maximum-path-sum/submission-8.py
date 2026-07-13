# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        self.res = -1001
        def dfs(cur):
            if not cur:
                return 0
            left = dfs(cur.left)
            right = dfs(cur.right)
            self.res = max(left+cur.val+right,cur.val,cur.val+right,cur.val+left,self.res)
            return max(left+cur.val,cur.val,cur.val+right)
        dfs(root)
        return self.res

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
        s = -1001
        def dfs(cur):
            nonlocal s
            if not cur:
                return -1001
            left = dfs(cur.left)
            right = dfs(cur.right)
            s = max(cur.val,cur.val+left+right,cur.val+left,cur.val+right,s)
            return max(cur.val,cur.val+left,cur.val+right)
        dfs(root)
        return s
        

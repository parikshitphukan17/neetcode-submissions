# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0
        def dfs(m,node):
            nonlocal res
            if not node:
                return
            if m<=node.val:
                res +=1
                m = node.val
            dfs(m,node.left)
            dfs(m,node.right)
        dfs(-101,root)
        return res



        # if m<node:
        #     +1
        # m = max(m,node)
        # go left and right
        
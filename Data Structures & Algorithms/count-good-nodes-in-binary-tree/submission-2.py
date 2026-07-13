# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0

        def dfs(node,maxVal):
            nonlocal res
            if not node:
                return

            maxVal = max(maxVal,node.val)
            if maxVal<= node.val:
                res +=1
            dfs(node.left,maxVal)
            dfs(node.right,maxVal)
        dfs(root,-101)
        return res

            
        
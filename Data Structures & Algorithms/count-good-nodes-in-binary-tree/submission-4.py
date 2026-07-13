# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(cur,maxVal):
            goodNodes = 0
            if not cur:
                return goodNodes
            if maxVal<=cur.val:
                goodNodes +=1
                maxVal = cur.val
            return goodNodes + dfs(cur.left,maxVal) + dfs(cur.right,maxVal)
        return dfs(root,-101)


        
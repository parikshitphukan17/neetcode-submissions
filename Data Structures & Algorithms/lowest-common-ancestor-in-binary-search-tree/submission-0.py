# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        self.res = None
        if p.val>q.val:
            self.left = q.val
            self.right = p.val
        else:
            self.right = q.val
            self.left = p.val
        def dfs(node):
            if self.res:
                return 
            if not node:
                return
            if node.val >= self.left and node.val<= self.right:
                self.res = node
                return
            elif node.val <self.left:
                return dfs(node.right)
            else:
                return dfs(node.left)
        dfs(root)
        return self.res
            

        
        
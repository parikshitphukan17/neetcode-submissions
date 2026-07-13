# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if p.val>q.val:
            p,q = q,p
        res = None
        def dfs(node):
            nonlocal res
            if not node or res:
                return
            if p.val <= node.val and node.val<=q.val:
                res = node
                return
            if p.val<node.val and q.val< node.val:
                dfs(node.left)
            else:
                dfs(node.right)
        dfs(root)
        return res

        
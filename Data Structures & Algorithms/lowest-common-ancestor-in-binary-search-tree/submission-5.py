# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        res = None
        if q.val<p.val:
            p,q = q,p
        
        def lcs(cur):
            nonlocal res
            if not cur:
                return 
            if p.val<=cur.val and cur.val<=q.val:
                res = cur
                return
            if q.val<cur.val:
                lcs(cur.left)
            else:
                lcs(cur.right)
        lcs(root)
        return res
            
            
        
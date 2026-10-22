# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if q.val<p.val:
            p,q=q,p
        def find(node,p,q):
            if node.val>=p.val and node.val<=q.val:
                return node
            if p.val<node.val:
                return find(node.left,p,q)
            return find(node.right,p,q)
        return find(root,p,q)
        
        
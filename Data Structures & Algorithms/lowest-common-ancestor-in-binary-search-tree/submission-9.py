# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if q.val<p.val:
            p,q = q,p
        def dfs(cur,p,q):
            if not cur:
                return
            if p.val>cur.val:
                return dfs(cur.right,p,q)
            elif q.val<cur.val:
                return dfs(cur.left,p,q)
            return cur
        return dfs(root,p,q)


        
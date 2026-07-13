# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        res = []
        cur = [root]
        while cur:
            next = []
            n = None
            while cur:
                n = cur.pop(0)
                if n.left:
                    next.append(n.left)
                if n.right:
                    next.append(n.right)
            res.append(n.val)
            cur = next
        return res

        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        res = []
        cur = [root]
        while cur:
            next = []
            curVal = []
            while cur:
                n = cur.pop(0)
                curVal.append(n.val)
                if n.left:
                    next.append(n.left)
                if n.right:
                    next.append(n.right)
            res.append(curVal)
            cur = next
        return res


        
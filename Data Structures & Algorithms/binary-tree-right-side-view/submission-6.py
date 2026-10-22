# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if not root:
            return res
        q = deque([root])
        while q:
            nextQ = deque([])
            res.append(q[-1].val)
            while q:
                cur = q.popleft()
                if cur.left:
                    nextQ.append(cur.left)
                if cur.right:
                    nextQ.append(cur.right)
            q = nextQ
        return res


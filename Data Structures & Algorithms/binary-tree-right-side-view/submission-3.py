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
        cur = deque([root])
        while cur:
            last = None
            child = deque([])
            while cur:
                node = cur.popleft()
                if node.left:
                    child.append(node.left)
                if node.right:
                    child.append(node.right)
                last = node.val
            res.append(last)
            cur = child
        return res

        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        if not root:
            return res
        q = deque([root])
        while q:
            children = deque([])
            level = []
            while q:
                cur = q.popleft()
                level.append(cur.val)
                if cur.left:
                    children.append(cur.left)
                if cur.right:
                    children.append(cur.right)
            res.append(level)
            q = children
        return res


        
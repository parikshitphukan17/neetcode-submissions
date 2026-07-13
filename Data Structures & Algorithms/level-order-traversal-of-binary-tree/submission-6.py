# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque()
        if not root:
            return []
        res = []
        q.append(root)
        while q:
            nextChild = deque()
            level = []
            while q:
                node = q.popleft()
                level.append(node.val)
                if node.left:
                    nextChild.append(node.left)
                if node.right:
                    nextChild.append(node.right)
            res.append(level)
            q = nextChild
        return res





        
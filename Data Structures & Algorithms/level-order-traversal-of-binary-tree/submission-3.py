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
        cur = deque([root])
        while cur:
            child = deque([])
            level = []
            while cur:
                node = cur.popleft()
                if node.left:
                    child.append(node.left)
                if node.right:
                    child.append(node.right)
                level.append(node.val)
            res.append(level)
            cur = child
        return res
                
        
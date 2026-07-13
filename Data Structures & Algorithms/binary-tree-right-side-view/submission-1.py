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

        level = deque([root])
        while level:
            nextLevel = deque([])
            right = None
            while level:
                right = level.popleft()
                if right.left:
                    nextLevel.append(right.left)
                if right.right:
                    nextLevel.append(right.right)
            res.append(right.val)
            level = nextLevel
        return res


        
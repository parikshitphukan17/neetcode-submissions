# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        pre = deque(preorder)
        def dfs(inorder):
            if not inorder:
                return None
            root = TreeNode(pre.popleft())
            index = inorder.index(root.val)
            root.left = dfs(inorder[:index])
            root.right = dfs(inorder[index+1:])
            return root
        return dfs(inorder)
    









#                             5
#             4                                7
#         2       1                    10              9
#            3        6              11    12      13     14




# [2,3,4,1,6,5,11,10,12,7,13,9,14]

# [5,4,2,3,1,6,7,10,11,12,9,13,14]

# root = 5
# left = [2,3,4,1,6] right = [5,11,10,12,7,13,9,14]


root = 4
left = [2,3]

root = 2
right = [3]

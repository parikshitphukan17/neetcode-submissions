# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        def dfs(ino):
            if not ino or not preorder:
                return
            root = TreeNode(preorder.pop(0))
            index = ino.index(root.val)
            root.left = dfs(ino[:index])
            root.right = dfs(ino[index+1:])
            return root
        return dfs(inorder)



        #                         1
        #         3                               6
        #     2       4                       7
        # -1                                        9

        # 1   2   3   4
        # 2   1   3   4

        # 2       3   4
        # 2       3   4


        # 3   4




        #get index for first node in preorder  in inorder

        #split into left and right
        #do recursively for left till left not empty
        #then go right         
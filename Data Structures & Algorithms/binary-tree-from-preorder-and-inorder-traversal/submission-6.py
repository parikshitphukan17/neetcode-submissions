# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        def build(inorder):
            if not inorder:
                return None
            root = TreeNode(preorder.pop(0))
            index = inorder.index(root.val)
            root.left = build(inorder[:index])
            root.right= build(inorder[index+1:])
            return root
        return build(inorder)



            #                             1
            #                 2                       5                
                    
            #         3              4            6       7




            #     3   2   4   1   6   5   7


            #     1   2   3   4   5   6   7


            # root 1
            #     3   2   4       6   5   7

            # root 2  
            #     3     4
            
            # root 3
            # None

            # root 4
            # None


            # root 5
            #     6       7


                
        
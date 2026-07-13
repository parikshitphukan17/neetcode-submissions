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
            left,right = inorder[:index],inorder[index+1:]
            root.left = build(left)
            root.right = build(right)
            return root
        return build(inorder)






        # [1,2,3,4]
        # [2,1,3,4]
        # n = popleft()
        # index = inorder.index(n)
        # left,right = inorder[:index],inorder[index+1:]        
        
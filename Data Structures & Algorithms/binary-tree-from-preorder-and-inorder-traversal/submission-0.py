# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def build(pre,inor):
            if not pre or not inor:
                return None
            
            root = TreeNode(pre.pop(0))
            index = inor.index(root.val)
            root.left = build(pre,inor[:index])
            root.right = build(pre,inor[index+1:])
            return root
        return build(preorder,inorder)
        
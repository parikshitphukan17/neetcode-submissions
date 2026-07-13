# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        stack = []
        def build(node):
            if not node:
                stack.append("#")
                return
            stack.append(str(node.val))
            build(node.left)
            build(node.right)
        build(root)
        return ",".join(stack)

        1,2,#,#,3,4,#,#,5,#,#

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        stack = data.split(",")
        def extract():
            if not stack or stack[0] == "#":
                if stack:
                    stack.pop(0)
                return None
            n = stack.pop(0)
            root = TreeNode(int(n))
            root.left = extract()
            root.right = extract()
            return root
        return extract()
            

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = []
        def preOrder(node):
            if not node:
                res.append("#")
                return
            res.append(str(node.val))
            preOrder(node.left)
            preOrder(node.right)
        
        preOrder(root)
        return ",".join(res)  



        



        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        nodes = deque(data.split(","))
        def build():
            if not nodes:
                return
            rootVal = nodes.popleft()
            if rootVal =="#":
                return 
            root = TreeNode(rootVal)
            root.left = build()
            root.right = build()
            return root
        return build()






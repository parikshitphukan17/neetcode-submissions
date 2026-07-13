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
        def dfs(cur):
            if not cur:
                stack.append("#")
                return
            stack.append(str(cur.val))
            dfs(cur.left)
            dfs(cur.right)
        dfs(root)
        return ",".join(stack)

        #1,2,#,#,3,4,#,#,5,#,#
       
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        stack = data.split(",")

        def build():
            if not stack:
                return
            cur = stack.pop(0)
            if cur == "#":
                return
            node = TreeNode(int(cur))
            node.left = build()
            node.right = build()
            return node
        return build()



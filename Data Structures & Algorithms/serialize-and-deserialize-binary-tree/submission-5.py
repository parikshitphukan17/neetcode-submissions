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
        def dfs(node):
            if not node:
                res.append("#")
                return
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return ",".join(res)

    #     12##34##5##
    #     1.   
    #    2
    #      #

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        inp = deque(data.split(","))
        def dfs():
            if not inp:
                return
            cur = inp.popleft()
            if cur == "#":
                return
            root = TreeNode(int(cur))
            root.left = dfs()
            root.right = dfs()
            return root
        return dfs()

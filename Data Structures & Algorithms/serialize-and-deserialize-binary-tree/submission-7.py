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
        def build(cur):
            if not cur:
                res.append("#")
                return
            res.append(str(cur.val))
            build(cur.left)
            build(cur.right)
        build(root)        
        return ",".join(res)


        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        nodes = data.split(",")
        def dfs():
            if not nodes:
                return None
            val = nodes.pop(0)
            if val == "#":
                return None
            root = TreeNode(int(val))
            root.left = dfs()
            root.right = dfs()
            return root
        return dfs()



    #                         1
    #             2                       5
    #         3       4               6       7



    #         1   2   3   #   #   4   #   #   5   6   #   #   7   #   #

    #                 1
    #     2                       5        
    # 3       4               6       7


    

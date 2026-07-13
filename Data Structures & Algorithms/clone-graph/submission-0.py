"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        def dfs(src,vis):
            if src in vis:
                return vis[src]
            root = Node(src.val)
            #print(root.val)
            vis[src] = root
            if src.neighbors:
                root.neighbors = []
                for nei in src.neighbors:
                    n = dfs(nei,vis)
                    if n:
                        root.neighbors.append(n)
            #print(root.val,root.neighbors)
            return root
        if not node:
            return
        return dfs(node,{})
        
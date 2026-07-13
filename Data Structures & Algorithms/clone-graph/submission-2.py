"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        mapper = {}
        def dfs(node):
            if not node:
                return
            if node in mapper:
                return mapper[node]
            mapper[node] = Node(node.val)
            copyNode = mapper[node]
            for child in node.neighbors:
                copyNode.neighbors.append(dfs(child))
            return copyNode
        return dfs(node)

        
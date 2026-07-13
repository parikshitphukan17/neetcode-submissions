class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = {i:[] for i in range(n)}
        for e1,e2 in edges:
            adj[e1].append(e2)
            adj[e2].append(e1)
        vis = set()
        def dfs(cur,src):
            if cur in vis:
                return False
            vis.add(cur)
            for node in adj[cur]:
                if node == src:
                    continue
                if not dfs(node,cur):
                    return False
            return True
        return dfs(0,-1) and len(vis) == n

        
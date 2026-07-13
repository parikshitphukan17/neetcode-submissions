class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) > n-1:
            return False

        adj = {i:[] for i in range(n)}
        for e1,e2 in edges:
            adj[e1].append(e2)
            adj[e2].append(e1)
        vis = set()
        def dfs(src,par):
            if src in vis:
                return False
            vis.add(src)
            for nei in adj[src]:
                if nei == par:
                    continue
                if not dfs(nei,src):
                    return False
            return True
        if not dfs(0,-1):
            return False
        return len(vis) == n

        

        
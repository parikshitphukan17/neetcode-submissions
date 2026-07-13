class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges)>n-1:
            return False

        adj = {i:[] for i in range(n)}
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        vis = set()
        def dfs(edge,par):
            if edge in vis:
                return False
            vis.add(edge)
            for child in adj[edge]:
                if child == par:
                    continue
                if not dfs(child,edge):
                    return False
            return True
        return dfs(0,-1) and len(vis) ==n

                


        
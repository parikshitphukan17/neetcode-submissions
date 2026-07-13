class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) > n-1:
            return False
        
        adj = defaultdict(list)
        for n1,n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)
        vis = {}
        def dfs(n,par):
            if n in vis:
                return vis[n]
            vis[n] = False
            for n2 in adj[n]:
                if n2 == par:
                    continue
                if not dfs(n2,n):
                    return False
            vis[n] = True
            return True
        
        if not dfs(0,-1):
            return False
        return len(vis) == n
        
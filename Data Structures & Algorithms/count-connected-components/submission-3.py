class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        adj = {i:[] for i in range(n)}
        vis = set()
        for e1,e2 in edges:
            adj[e1].append(e2)
            adj[e2].append(e1)
        def dfs(e,par):
            if e in vis:
                return
            vis.add(e)
            for child in adj[e]:
                if child == par:
                    continue
                dfs(child,e)
        res = 0
        for i in range(n):
            if i not in vis:
                res +=1
                dfs(i,-1)
        print(adj)
        return res        
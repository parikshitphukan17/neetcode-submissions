class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = {i:[] for i in range(n)}
        for e1,e2 in edges:
            adj[e1].append(e2)
            adj[e2].append(e1)
        vis = set()
        def dfs(e):
            if e in vis:
                return
            vis.add(e)
            for nei in adj[e]:
                dfs(nei)
        res = 0
        for e in range(n):
            if e not in vis:
                res +=1
                dfs(e)
        return res

        
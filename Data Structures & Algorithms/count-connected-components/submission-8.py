class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        vis = set()
        adj = {i:[] for i in range(n)}
        def dfs(n):
            if n in vis:
                return
            vis.add(n)
            for nei in adj[n]:
                dfs(nei)
        for n1,n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)
        res = 0
        for i in range(n):
            if i not in vis:
                res+=1
                dfs(i)
        return res

        
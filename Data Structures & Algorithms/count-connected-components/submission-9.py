class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        adj = {i:[] for i in range(n)}
        for e1,e2 in edges:
            adj[e1].append(e2)
            adj[e2].append(e1)
        vis = set()
        def dfs(node):
            if node in vis:
                return
            vis.add(node)
            for nei in adj[node]:
                dfs(nei)
            return
        
        res = 0
        for i in range(n):
            if i not in vis:
                res+=1
                dfs(i)
        return res

        
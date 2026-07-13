class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        vis = set()
        adj = {i:[] for i in range(n)}
        for e1,e2 in edges:
            adj[e1].append(e2)
            adj[e2].append(e1)

        def dfs(cur,par):
            if cur in vis:
                return
            vis.add(cur)
            for node in adj[cur]:
                if node == par:
                    continue
                dfs(node,cur)
        

        res = 0
        for i in range(n):
            if i not in vis:
                res +=1
                dfs(i,-1)
        return res

        
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        for e1,e2 in edges:
            adj[e1].append(e2)
            adj[e2].append(e1)
        vis = set()
        def dfs(src,e):
            if e in vis:
                return
            vis.add(e)
            for nei in adj[e]:
                if nei == src:
                    continue
                dfs(e,nei)
        res = 0
        for e in range(n):
            if e not in vis:
                res+=1
                dfs(-1,e)
        return res

        
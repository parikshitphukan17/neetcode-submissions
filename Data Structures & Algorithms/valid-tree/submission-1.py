class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges)> n-1:
            return False
        adj={i:[] for i in range(n)}
        for e1,e2 in edges:
            adj[e1].append(e2)
            adj[e2].append(e1)
        vis = set()
        def dfs(i,parent):
            if i in vis:
                return False
            vis.add(i)
            for nei in adj[i]:
                if nei == parent:
                    continue
                if not dfs(nei,i):
                    return False
            return True
        
        return True if dfs(0,-1) and len(vis) == n else False


        
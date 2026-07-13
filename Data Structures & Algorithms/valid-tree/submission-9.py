class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = {i:[] for i in range(n)}
        for e1,e2 in edges:
            adj[e1].append(e2)
            adj[e2].append(e1)
        vis = set()
        def dfs(e,parent):
            if e in vis:
                return False
            vis.add(e)
            for nei in adj[e]:
                if nei == parent:
                    continue
                if not dfs(nei,e):
                    return False
            return True
        
        
        return dfs(0,-1) and len(vis) == n

        #     0
        # 1   2   3
        # 4

        
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = defaultdict(list)
        for e1,e2 in edges:
            adj[e1].append(e2)
            adj[e2].append(e1)
        vis = set()
        def dfs(src,e):
            if e in vis:
                return False
            vis.add(e)
            for nei in adj[e]:
                if nei == src:
                    continue
                if not dfs(e,nei):
                    return False
            return True
        
        return dfs(-1,0) and len(vis) == n

            

        
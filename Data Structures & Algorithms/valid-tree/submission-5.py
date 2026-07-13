class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges)>n-1:
            return False
        adj = defaultdict(list)
        for n1,n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)
        vis = set()
        def dfs(n,p):
            if n in vis:
                return False
            vis.add(n)
            for nei in adj[n]:
                if nei == p:
                    continue
                if not dfs(nei,n):
                    return False
            return True
        if not dfs(0,-1):
            return False
        return len(vis) == n


        
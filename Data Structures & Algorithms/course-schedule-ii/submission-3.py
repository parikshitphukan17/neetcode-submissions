class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        res = []
        vis = {}
        for c,p in prerequisites:
            adj[c].append(p)
        def dfs(n):
            if n in vis:
                return vis[n]
            vis[n] =False
            for nei in adj[n]:
                if not dfs(nei):
                    return False
            vis[n] = True
            res.append(n)
            return True
        for n in range(numCourses):
            if not dfs(n):
                return []
        return res
        
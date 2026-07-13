class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {i:[] for i in range(numCourses)}
        vis = {}
        def dfs(c):
            if c in vis:
                return vis[c]
            vis[c] = False
            for nei in adj[c]:
                if not dfs(nei):
                    return False
            vis[c] = True
            adj[c] = []
            return True
        for c,p in prerequisites:
            adj[c].append(p)
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
        
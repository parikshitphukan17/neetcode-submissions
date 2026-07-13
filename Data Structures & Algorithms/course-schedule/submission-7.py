class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {i:[] for i in range(numCourses)}
        for crs,pre in prerequisites:
            adj[crs].append(pre)
        vis = {}
        def dfs(crs):
            if crs in vis:
                return vis[crs]
            vis[crs] = False
            for pre in adj[crs]:
                if not dfs(pre):
                    return False
            vis[crs] = True
            return True
        for n in range(numCourses):
            if not dfs(n):
                return False
        return True
        
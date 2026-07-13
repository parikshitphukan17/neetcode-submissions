class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        vis = {}
        adj = {i:[] for i in range(numCourses)}
        for crs,pre in prerequisites:
            adj[crs].append(pre)
        def dfs(crs):
            if crs in vis:
                return vis[crs]
            if not adj[crs]:
                return True
            vis[crs] = False
            for pre in adj[crs]:
                if not dfs(pre):
                    return False
            vis[crs] = True
            return True
        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True
        
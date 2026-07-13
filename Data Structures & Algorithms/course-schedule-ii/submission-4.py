class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = {i:[] for i in range(numCourses)}
        for crs,pre in prerequisites:
            adj[crs].append(pre)
        
        vis = {}
        res = []
        def dfs(cur):
            if cur in vis:
                return vis[cur]
            vis[cur] = False
            for pre in adj[cur]:
                if not dfs(pre):
                    return False
            vis[cur] = True
            res.append(cur)
            return True
        for i in range(numCourses):
            if not dfs(i):
                return []
        return res



        
        
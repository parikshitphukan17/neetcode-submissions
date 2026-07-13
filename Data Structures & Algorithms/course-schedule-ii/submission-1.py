class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = {i:[] for i in range(numCourses)}
        for crs,pre in prerequisites:
            adj[crs].append(pre)
        vis = set()
        cycle = set()
        res = []
        def dfs(crs):
            if crs in vis:
                return True
            if crs in cycle:
                return False
            cycle.add(crs)
            for nei in adj[crs]:
                if not dfs(nei):
                    return False
            vis.add(crs)
            res.append(crs)
            cycle.remove(crs)
            return True
        for c in range(numCourses):
            if not dfs(c):
                return []
        return res
                        
        
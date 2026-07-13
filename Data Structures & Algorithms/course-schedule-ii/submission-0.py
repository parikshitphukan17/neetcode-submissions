class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        preMap = {i:[] for i in range(numCourses)}
        for crs,pre in prerequisites:
            preMap[crs].append(pre)
        res = []

        cycle,vis = set(),set()
        def dfs(crs):
            if crs in cycle:
                return False
            if crs in vis:
                return True

            cycle.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            vis.add(crs)
            res.append(crs)
            cycle.remove(crs)
            return True
        for c in range(numCourses):
            if not dfs(c):
                return []
        return res
            
            
        
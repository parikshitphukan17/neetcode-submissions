class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i:[] for i in range(numCourses)}
        vis = set()
        for crs,pre in prerequisites:
            preMap[crs].append(pre)

        def dfs(crs):
            if crs in vis:
                return False
            if preMap[crs] == []:
                return True
            vis.add(crs)
            for pre in preMap[crs]:
                
                if not dfs(pre):
                    return False
            vis.remove(crs)
            preMap[crs] = []
            return True
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True
        
            
            

        
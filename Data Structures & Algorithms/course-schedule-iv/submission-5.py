class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = {i:[] for i in range(numCourses)}
        for c1,c2 in prerequisites:
            adj[c1].append(c2)
        ind = {}

        def dfs(src):
            if src in ind:
                return ind[src]
            ind[src] = set()
            for nei in adj[src]:
                ind[src] |= dfs(nei)
                ind[src].add(nei)
            return ind[src]
        for i in range(numCourses):
            dfs(i)

        # 1->0
        # 2->1
        # 3->2
        res = []
        for c1,c2 in queries:
            res.append(c2 in ind[c1])
        return res
        




# 1->2
# 1->0
# 2->0





        
     
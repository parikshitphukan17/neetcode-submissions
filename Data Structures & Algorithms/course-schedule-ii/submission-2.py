class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        vis = {}
        adj = defaultdict(list)
        for c1,c2 in prerequisites:
            adj[c1].append(c2)
        res = []
        def dfs(c):
            if c in vis:
                return vis[c]
            vis[c] = False
            for c2 in adj[c]:
                if not dfs(c2):
                    return False
                
            vis[c] = True
            res.append(c)
            return True
        for i in range(numCourses):
            if not dfs(i):
                return []
        return res


        
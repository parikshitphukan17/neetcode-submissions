class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        dir = [[0,1],[1,0],[0,-1],[-1,0]]
        res = 0
        N,M = len(grid),len(grid[0])
        def dfs(i,j):
            if i<0 or j<0 or i==N or j==M or grid[i][j] == 0:
                return 0
            cur = 1
            grid[i][j] = 0
            for dx,dy in dir:
                cur += dfs(i+dx,j+dy)
            return cur
        
        for i in range(N):
            for j in range(M):
                res = max(res,dfs(i,j))
        return res

        
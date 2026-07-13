class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        N,M = len(grid),len(grid[0])
        dire = [[0,1],[1,0],[-1,0],[0,-1]]
        def dfs(i,j):
            if i<0 or j<0 or i == N or j==M or grid[i][j] == 0:
                return 0
            grid[i][j] = 0
            path = 1
            for dx,dy in dire:
                path += dfs(i+dx,j+dy)
            return path
        res = 0
        for i in range(N):
            for j in range(M):
                res = max(res,dfs(i,j))
        return res
        
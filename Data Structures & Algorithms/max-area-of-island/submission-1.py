class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res,N,M = 0,len(grid),len(grid[0])
        direc = [[0,1],[1,0],[0,-1],[-1,0]]
        def dfs(i,j):
            if i<0 or i>=N or j<0 or j>=M or grid[i][j] ==0:
                return 0
            grid[i][j] = 0
            a = 1
            for dx,dy in direc:
                a += dfs(i+dx,j+dy)
            return a
        for x in range(N):
            for y in range(M):
                if grid[x][y] == 1:
                    res = max(res,dfs(x,y))
        return res
        
        

        
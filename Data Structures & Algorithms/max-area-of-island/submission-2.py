class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        dire = [[0,1],[1,0],[-1,0],[0,-1]]
        N,M = len(grid),len(grid[0])
        def dfs(i,j):
            if i<0 or j<0 or i ==N or j==M or grid[i][j] == 0:
                return 0
            grid[i][j] = 0
            res = 1
            for dx,dy in dire:
                res += dfs(dx+i,j+dy)
            return res
        area = 0
        for i in range(N):
            for j in range(M):
                if grid[i][j] == 1:
                    area = max(area,dfs(i,j))
        return area

        
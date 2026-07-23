class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        dir = [[0,1],[1,0],[-1,0],[0,-1]]

        M,N = len(grid),len(grid[0])
        self.res = 0
        def dfs(i,j):
            if i<0 or j<0 or i==M or j==N  or grid[i][j]==0:
                return 0
            grid[i][j] = 0
            cur = 1
            for dx,dy in dir:
                cur += dfs(i+dx,j+dy)
            self.res = max(self.res,cur)
            return cur
        for i in range(M):
            for j in range(N):
                dfs(i,j)
        return self.res
            

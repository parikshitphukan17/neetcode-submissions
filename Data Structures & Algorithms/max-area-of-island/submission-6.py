class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        dir = [[0,1],[1,0],[0,-1],[-1,0]]
        M,N = len(grid),len(grid[0])
        def dfs(i,j):
            if i<0 or i==M or j<0 or j==N or not grid[i][j]:
                return 0
            grid[i][j] = 0
            cur = 1
            for dx,dy in dir:
                cur += dfs(i+dx,j+dy)
            return cur
        for i in range(M):
            for j in range(N):
                res = max(res,dfs(i,j))
        return res
        
            
        
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        M,N = len(grid),len(grid[0])
        dir = [[0,1],[1,0],[-1,0],[0,-1]]
        def dfs(i,j):
            if i<0 or i==M or j<0 or j==N or grid[i][j] != "1":
                return
            grid[i][j] = "0"
            for dx,dy in dir:
                dfs(i+dx,j+dy)
        res = 0

        for i in range(M):
            for j in range(N):
                if grid[i][j] == "1":
                    res+=1
                    dfs(i,j)
        return res






        
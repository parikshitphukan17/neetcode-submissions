class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        direc = [[0,1],[-1,0],[1,0],[0,-1]]
        N,M = len(grid),len(grid[0])
        def dfs(i,j):
            if i>=N or i<0 or j>=M or j<0 or grid[i][j] == "0":
                return
            grid[i][j] = "0"
            for dx,dy in direc:
                dfs(i+dx,j+dy)
        res = 0
        for x in range(N):
            for y in range(M):
                if grid[x][y] == "1":
                    res +=1
                    dfs(x,y)
        return res


        
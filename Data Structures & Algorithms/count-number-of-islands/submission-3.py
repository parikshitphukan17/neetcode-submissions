class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        N,M = len(grid),len(grid[0])
        dire = [[0,1],[1,0],[-1,0],[0,-1]]
        def dfs(i,j):
            if i<0 or j<0 or i == N or j ==M or grid[i][j] == "0":
                return 
            grid[i][j] = "0"
            for dx,dy in dire:
                dfs(i+dx,j+dy)
        
        res = 0
        for i in range(N):
            for j in range(M):
                if grid[i][j] == "1":
                    res +=1
                    dfs(i,j)
        return res
        
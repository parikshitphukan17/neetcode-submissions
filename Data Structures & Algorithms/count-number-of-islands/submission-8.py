class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        M,N=len(grid),len(grid[0])
        def dfs(i,j):
            if i==M or j==N or i<0 or j<0 or grid[i][j] == "0":
                return
            grid[i][j] = "0"
            dfs(i+1,j)
            dfs(i-1,j)
            dfs(i,j+1)
            dfs(i,j-1)
        for i in range(M):
            for j in range(N):
                if grid[i][j] == "1":
                    res +=1
                    dfs(i,j)
        return res
        
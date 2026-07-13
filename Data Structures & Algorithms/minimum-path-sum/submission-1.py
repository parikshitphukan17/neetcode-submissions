class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        M,N = len(grid),len(grid[0])
        dp = [[float("inf")]* (N+1) for _ in range(M+1)]
        dp[M-1][N-1] = grid[M-1][N-1]
        for i in range(M-1,-1,-1):
            for j in range(N-1,-1,-1):
                dp[i][j] = min(dp[i][j], grid[i][j]+ min(dp[i+1][j],dp[i][j+1]))
        return dp[i][j]
        # def dfs(i,j):
        #     if i==M-1 and j ==N-1:
        #         return grid[i][j]
        #     if i==M or j==N:
        #         return float("inf")
        #     if (i,j) in dp:
        #         return dp[(i,j)]
        #     dp[(i,j)] = grid[i][j] + min(dfs(i+1,j),dfs(i,j+1))
        #     return dp[(i,j)]
        # return dfs(0,0)

        
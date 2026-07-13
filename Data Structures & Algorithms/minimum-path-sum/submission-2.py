class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        M,N = len(grid),len(grid[0])
        dp = [float("inf")]* (N+1)
        for i in range(M-1,-1,-1):
            cur = [float("inf")]* (N+1)
            cur[N-1] = grid[M-1][N-1] if M-1 == i else float("inf")
            for j in range(N-1,-1,-1):
                cur[j] = min(cur[j], grid[i][j]+ min(dp[j],cur[j+1]))
            dp = cur
        return dp[j]
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

        
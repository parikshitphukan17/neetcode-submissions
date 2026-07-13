class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        dp = {}
        M,N = len(grid),len(grid[0])
        def dfs(i,j):
            if i==M-1 and j ==N-1:
                return grid[i][j]
            if i==M or j==N:
                return float("inf")
            if (i,j) in dp:
                return dp[(i,j)]
            dp[(i,j)] = grid[i][j] + min(dfs(i+1,j),dfs(i,j+1))
            return dp[(i,j)]
        return dfs(0,0)

        
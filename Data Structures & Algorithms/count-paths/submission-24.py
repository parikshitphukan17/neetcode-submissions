class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        vis = {}
        def dfs(i,j):
            nonlocal m,n
            if (i,j) in vis:
                return vis[(i,j)]
            if i == m+1 or j == n+1:
                return 0
            if i == m and j == n:
                return 1
            vis[(i,j)] = dfs(i+1,j) + dfs(i,j+1)
            return vis[(i,j)]
        return dfs(1,1)
            
                
        
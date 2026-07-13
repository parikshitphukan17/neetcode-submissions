class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        dp = {}
        N,M = len(matrix),len(matrix[0])
        dire = [[0,1],[1,0],[-1,0],[0,-1]]
        def dfs(i,j,prev):
            if i<0 or j<0 or i==N or j==M or prev>= matrix[i][j]:
                return 0
            if (i,j) in dp:
                return dp[(i,j)]
            path = 1
            for dx,dy in dire:
                path = max(path,1+dfs(i+dx,j+dy,matrix[i][j]))
            dp[(i,j)] = path
            return dp[(i,j)]
        res = 0
        for i in range(N):
            for j in range(M):
                    res = max(res,dfs(i,j,-1))
        return res

        
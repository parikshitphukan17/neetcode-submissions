class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        dp = {}
        N,M = len(matrix),len(matrix[0])
        dir = [[0,1],[1,0],[0,-1],[-1,0]]
        def dfs(i,j,last):
            if i<0 or j<0 or i==N or j==M or last>= matrix[i][j]:
                return 0
            if (i,j) in dp:
                return dp[(i,j)]
            dp[(i,j)] = 1
            maxNei = 0
            for dx,dy in dir:
                maxNei= max(dfs(i+dx,j+dy,matrix[i][j]),maxNei)
            dp[(i,j)] += maxNei
            return dp[(i,j)]
        res = 0
        for i in range(N):
            for j in range(M):
                res = max(res,dfs(i,j,-1))
        return res
        
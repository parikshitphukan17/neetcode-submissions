class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        N,M = len(matrix),len(matrix[0])
        dir = [[0,1],[1,0],[0,-1],[-1,0]]
        dp = {}
        def dfs(i,j,prev):
            if i <0 or j<0 or i==N or j ==M or matrix[i][j]<=prev:
                return 0
            if (i,j) in dp:
                return dp[(i,j)]
            maxNei = 0
            for dx,dy in dir:
                maxNei = max(maxNei,dfs(i+dx,j+dy,matrix[i][j]))
            dp[(i,j)] = 1+maxNei
            return dp[(i,j)]

        res = 0
        for i in range(N):
            for j in range(M):
                res = max(res,dfs(i,j,-1))
        return res
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:

        dir = [[0,1],[1,0],[0,-1],[-1,0]]
        dp = {}
        maxVal = 0
        M,N = len(matrix),len(matrix[0])
        def dfs(i,j,prev):
            nonlocal maxVal
            if i<0 or j<0 or i==M or j==N or matrix[i][j]<= prev:
                return 0
            if (i,j) in dp:
                return dp[(i,j)]
            cur = 1
            nei = 0
            for dx,dy in dir:
                nei = max(nei,dfs(i+dx,j+dy,matrix[i][j]))
            dp[(i,j)] = cur+nei
            return dp[(i,j)]
        for i in range(M):
            for j in range(N):
                maxVal = max(maxVal,dfs(i,j,-1))
        return maxVal

            

            

        
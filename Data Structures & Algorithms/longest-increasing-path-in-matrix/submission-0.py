class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        dp = {}
        dire = [[1,0],[0,1],[-1,0],[0,-1]]
        N,M = len(matrix),len(matrix[0])
        def dfs(i,j):
            
            if (i,j) in dp:
                return dp[(i,j)]
            path = 0
            for dx,dy in dire:
                x,y = i+dx,j+dy
                if x>=N or x<0 or y<0 or y>=M or matrix[x][y]<=matrix[i][j]:
                    continue
                path = max(path,dfs(x,y))
            dp[(i,j)] = 1+path
            return dp[(i,j)]
        res = 0
        for i in range(N):
            for j in range(M):
                res = max(res,dfs(i,j))
        return res

        
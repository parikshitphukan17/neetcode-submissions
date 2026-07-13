class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        dp = {}
        res = 0
        dir = [[0,1],[1,0],[0,-1],[-1,0]]
        M,N = len(matrix),len(matrix[0])
        def dfs(i,j):
            if (i,j) in dp:
                return dp[(i,j)]
            cur = 1
            next = 0
            for dx,dy in dir:
                x,y = i+dx,j+dy
                if x<0 or x ==M or y<0 or y ==N or matrix[x][y]<=matrix[i][j]:
                    continue
                next= max(dfs(x,y),next)
            
            dp[(i,j)] = cur+next
            return dp[(i,j)]
        for i in range(M):
            for j in range(N):
                res = max(res,dfs(i,j))
        return res
                

            



        
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        dp = {}
        dir = [[0,1],[1,0],[0,-1],[-1,0]]
        M,N = len(matrix),len(matrix[0])
        vis = set()
        res = 0
        def dfs(i,j,prev):
            nonlocal res
            if (i,j) in dp:
                return dp[(i,j)]
            if i<0 or j<0 or i==M or j==N or (i,j) in vis or matrix[i][j]<=prev:
                return 0
            vis.add((i,j))
            cur =0
            for dx,dy in dir:
                cur= max(cur,dfs(i+dx,j+dy,matrix[i][j])+1)
            vis.remove((i,j))
            res = max(res,cur)
            return cur
        
        for i in range(M):
            for j in range(N):
                dfs(i,j,-1)
        return res

        
            
        
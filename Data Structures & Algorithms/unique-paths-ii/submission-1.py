class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        dp = {}
        M,N = len(obstacleGrid),len(obstacleGrid[0])
        def dfs(i,j):
            if (i,j) in dp:
                return dp[(i,j)]
            if i ==M or j ==N:
                return 0
            
            if obstacleGrid[i][j] == 1:
                dp[(i,j)] = 0
            elif i==M-1 and j==N-1:
                return 1
            else:
                dp[(i,j)] = dfs(i+1,j)+ dfs(i,j+1)
            return dp[(i,j)]
        return dfs(0,0)
            


        
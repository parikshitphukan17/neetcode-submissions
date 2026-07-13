import sys
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        M,N = len(matrix),len(matrix[0])
        def set(i,j):
            for x in range(M):
                if matrix[x][j] == 0:
                    continue
                matrix[x][j] = sys.maxsize
    
            for y in range(N):
                if matrix[i][y] == 0:
                    continue
                matrix[i][y] = sys.maxsize
        
        for i in range(M):
            for j in range(N):
                if matrix[i][j] == 0:
                    set(i,j)
        
        for i in range(M):
            for j in range(N):
                if matrix[i][j] == sys.maxsize:
                    matrix[i][j] = 0



                    # 0   1   2   0               0   0   0   0
                    # 3   4   5   2               0   4   5   0
                    # 1   3   1   5               0   3   1   0

                    

         




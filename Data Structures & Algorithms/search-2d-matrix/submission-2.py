class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        N,M = len(matrix),len(matrix[0])
        row = None
        for i in range(N):
            if matrix[i][0]<= target and target<=matrix[i][M-1]:
                row = matrix[i]
                break
        if row == None:
            return False
        l,r = 0,M-1
        while l<=r:
            m = (l+r)//2
            if row[m]<target:
                l = m+1
            elif row[m]>target:
                r = m-1
            else:
                return True
        return False
            

        
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        N,M = len(matrix),len(matrix[0])
        search = None
        for i in range(N):
            if matrix[i][0]<=target and matrix[i][M-1]>=target:
                search = i
                break
        if search is None:
            return False
        
        row = matrix[i]
        l,r= 0,M-1
        while l<=r:
            m = (l+r)//2
            if row[m]<target:
                l =m+1
            elif row[m]>target:
                r =m-1
            else:
                return True
        return False



        
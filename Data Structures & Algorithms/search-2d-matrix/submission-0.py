class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(len(matrix)):
            if matrix[i][-1]>target and matrix[i][0]>target:
                return False
            if matrix[i][-1]<target or matrix[i][0]>target:
                continue
            l,r=0,len(matrix[i])-1
            while l<=r:
                mid = (l+r)//2
                midVal = matrix[i][mid]
                if midVal>target:
                    r=mid-1
                elif midVal<target:
                    l=mid+1
                else:
                    return True
        return False
        
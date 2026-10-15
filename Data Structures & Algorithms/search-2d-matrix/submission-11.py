class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l,r = 0,len(matrix)-1

        def found(row,target):
            l,r = 0,len(row)-1
            while l<=r:
                m = (l+r)//2
                val = row[m]
                if val<target:
                    l = m+1
                elif val>target:
                    r = m-1
                else:
                    return True
            return False
        while l<=r:
            m = (l+r)//2
            val = matrix[m][0]
            if val<=target:
                if matrix[m][-1]<target:
                    l=m+1
                elif found(matrix[m],target):
                    return True
                else:
                    l=m+1
            else:
                r =m-1
        return False
    
        
        
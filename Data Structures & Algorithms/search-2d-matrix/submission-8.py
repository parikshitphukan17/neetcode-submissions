class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:


        def bin(row):
            l,r = 0,len(row)-1
            while l<=r:
                m = (l+r)//2
                if target<row[m]:
                    r = m-1
                elif target>row[m]:
                    l = m+1
                else:
                    return True
            return False
        
        l,r = 0,len(matrix)-1
        while l<=r  and matrix[l][0] <= target :
            m = (l+r)//2
            if matrix[m][0]>target:
                r = m-1
            elif matrix[m][-1]<target:
                l = m+1
            else:
                if bin(matrix[m]):
                    return True
                l = m+1

        return False
                




        









        # 1.            
        # 10
        # 14
        # 18
        # 21

        
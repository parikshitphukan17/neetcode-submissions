class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        h1,h2 = 0,len(matrix)-1
        r = len(matrix[0])-1
        def search(row):
            nonlocal target
            l,r = 0, len(row)-1
            while l<=r:
                m = (l+r)//2
                if row[m] == target:
                    return True
                elif row[m] < target:
                    l =m+1
                else:
                    r = m-1
            return False
        while h1<=h2:
            mh = (h1+h2)//2
            if matrix[mh][0]>target:
                h2 = mh-1
            elif matrix[mh][0]<=target:
                if matrix[mh][r] < target:
                    h1 = mh+1
                else:
                    if search(matrix[mh]):
                        return True
                    h1 = mh+1
        return False 


        
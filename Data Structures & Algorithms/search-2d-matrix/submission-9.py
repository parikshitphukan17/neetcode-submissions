class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def find(matrix):
            l,r = 0,len(matrix)-1
            while l<=r:
                mid = (l+r)//2
                if matrix[mid]<target:
                    l = mid+1
                elif matrix[mid]>target:
                    r = mid-1
                else:
                    return True
            return False


        l,r = 0,len(matrix)-1
        while l<=r:
            mid = (l+r)//2
            if matrix[mid][0]<=target:
                if matrix[mid][-1]>=target and find(matrix[mid]):
                    return True
                l = mid+1
            else:
                r = mid -1
        return False

        

        
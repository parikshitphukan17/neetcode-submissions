class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        L,R,T,B = 0,len(matrix[0])-1,0,len(matrix)-1
        res = []
        # l,r = 1,1
        # t,b = 2,1
        # 1   2   3   4
        # 5   6   7   8
        # 9   10  11  12
        while L<=R and T<=B:
            for j in range(L,R+1):
                res.append(matrix[T][j])
            T+=1
            for i in range(T,B+1):
                res.append(matrix[i][R])
            R-=1
            if T<=B:

                for j in range(R,L-1,-1):
                    res.append(matrix[B][j])
                B-=1
            if L<=R:
                for i in range(B,T-1,-1):
                    res.append(matrix[i][L])
                L+=1
        return res
        



            

            

    # l,r = 0,2
    # t,b = 0,2
    #     1   2   3   4
    #     5   6   7   8
    #     9   10  11  12


    #     l to r

    #     1   2   3   4
    #     t+1 

    #     t to b
    #     r - 1

    #     r to l
    #     b-1

    #     b to t
    #     l+1


        
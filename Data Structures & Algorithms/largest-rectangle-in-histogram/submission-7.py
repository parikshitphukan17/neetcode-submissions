class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        res = 0
        # [7, 1,  7,  2,  2,  4]
        # [0,7]    i= 0.    7
        # [0,1]    i = 1
        # [2,7].   i = 2
        # [4,2]    i = 3

        for i,h in enumerate(heights):
            l = i
            while stack and stack[-1][1]>=h:
                l,val = stack.pop()
                res = max(res,(i-l)*val)
            stack.append([l,h])
        r = len(heights)
        while stack:
            l,val = stack.pop()
            res = max(res,(r-l)*val)
        return res



        #7      #7              


                    #4      #4      
                        #2          #2
                        
            #1
        

        # stack
        # index,h.     i              max A
        # 0     7.     0              0
        # 1     1      1               
        # pop till last in stack<cur and calc area for popped and take index as last popped index

        # stack
        # index,h.     i              max A
        # 0     1      1               7
        # 2     7      2              7
        # 3     4      3



        # stack
        # index,h.     i      max A
        # 0     1      1       7
        # 2     4      3.      7
        # 4     2      4     


        # stack
        # index,h.     i      max A
        # 0     1      1       7
        # 2     2      4       8
        # 5     4      5       8
        # 6     2          


        # stack
        # index,h.     i      max A
        # 0     1      1       7
        # 2     2      4       8
        # 5     4      5       8
        # 6     2.     6         


        # stack
        # index,h.     i      max A
        # 0     1      1       7
        # 2     2      6       max(8,(6-5)*4,(6-2)*2) = 8



        # 6-2 4 * 2
                  
        






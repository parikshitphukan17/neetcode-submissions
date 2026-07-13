class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        res = 0
        stack = []
        for i in heights:
            if not stack:
                stack.append([i,1])
                print(i,stack)
                continue
            breadth = 0
            while stack and i<stack[-1][0]:
                l,breadth = stack.pop()
                res = max(res,l*breadth)
            for j in range(len(stack)):
                l,b = stack[j]
                stack[j] = [l,b+1]
            if not stack or stack[-1][0]<i:
                stack.append([i,breadth+1])
        while stack:
            l,b = stack.pop()
            res = max(res,l*b)
        return res            
                
                




        # 7     7

        #                 4
        #          2  2
        #    1.      
        

        # stack = [[l,b]]
        #if greater val then stack:
        #while val > increase all b by 1 and add to stack
        #if lesser start poping and calc area till val not less
        #from less than equal to point increase b again
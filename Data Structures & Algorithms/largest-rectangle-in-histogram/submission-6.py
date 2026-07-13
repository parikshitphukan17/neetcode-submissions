class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:




        # 7       7

        #                     4

        #             2   2   
        #     1

        n = len(heights)
        stack = []

        leftMost = [-1] * n
        for i in range(n):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if stack:
                leftMost[i] = stack[-1]
            stack.append(i)

        stack = []
        rightMost = [n] * n
        for i in range(n - 1, -1, -1):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if stack:
                rightMost[i] = stack[-1]
            stack.append(i)

        maxArea = 0
        for i in range(n):
            leftMost[i] += 1
            rightMost[i] -= 1
            maxArea = max(maxArea, heights[i] * (rightMost[i] - leftMost[i] + 1))
        return maxArea
                
                




        # 7     7

        #                 4
        #          2  2
        #    1.      
        

        # stack = [[l,b]]
        #if greater val then stack:
        #while val > increase all b by 1 and add to stack
        #if lesser start poping and calc area till val not less
        #from less than equal to point increase b again
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        area = 0
        for i,h in enumerate(heights):
            index = i
            while stack and stack[-1][1]>=h:
                prevIndex, prevVal = stack.pop()
                index = prevIndex
                area = max(area,(i-prevIndex)*prevVal)
            stack.append([index,h])
        l = len(heights)
        while stack:
            prevIndex,prevVal = stack.pop()
            area = max(area,(l-prevIndex)*prevVal)
        return area



#         [[1,0]].  [7,2].  area = 7
# ------------
#         [[1,0],[7,2]], [2,3] 

#         [[1,0],[2,2]].   area = 7
# ------------
#         [[1,0],[2,2]].  [2,4]
#         [[1,0],[2,2]].  area = 7
# ---   ----
#         [[1,0],[2,2],[4,5]]


#         4*1
#         2*4 = 8
#         in end pop from stack and len - ind * cur

        

        
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        area = 0
        l,r = 0,len(heights)-1
        while l<r:
            l1,l2 = heights[l],heights[r]
            area = max(area,(r-l)*min(l1,l2))
            if l1<l2:
                l+=1
            else:
                r-=1
        return area
        
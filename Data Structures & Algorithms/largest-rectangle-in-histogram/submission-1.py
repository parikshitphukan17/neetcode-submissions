class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res = []
        area = 0
        for i in heights[::-1]:
            print(i,res,area)
            if not res:
                res.append([i,1])
                continue
            curB=1
            while res and res[-1][0]>i:
                l,b = res.pop()
                area = max(area,l*b)
                curB = max(curB,b+1)
            if not res:
                res.append([i,curB])
                continue
            j= len(res)-1
            if res[j][0] == i:
                res[j][1] +=1
                curB = 0
                j-=1
            while j>=0 and res[j][0]<i:
                res[j][1] +=1
                j-=1
            if curB:
                res.append([i,curB])
        while res:
            l,b = res.pop()
            area = max(area,l*b)
        return area
            
            

        
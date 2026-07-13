class Solution:
    def trap(self, height: List[int]) -> int:
        maxLeftSub,maxRightSub = [0]*len(height),[0]*len(height)
        i,j = 1,len(height)-2
        maxLeft,maxRight = 0,0
        res = 0
        while i<len(height):
            maxLeft = max(maxLeft,height[i-1])
            maxLeftSub[i] = maxLeft
            maxRight = max(maxRight,height[j+1])
            maxRightSub[j] = maxRight
            i +=1
            j -=1
        for i in range(0,len(height)):
            water = min(maxLeftSub[i],maxRightSub[i]) - height[i]
            if water>0:
                res += water
        return res



        
        
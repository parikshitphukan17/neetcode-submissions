class Solution:
    def trap(self, height: List[int]) -> int:
        maxLeft,maxRight = height[0],height[len(height)-1]
        l,r = 0,len(height)-1
        res =0
        while l<r:
            minVal = min(maxLeft,maxRight)
            if maxLeft<maxRight:
                l +=1
                res += max(0,minVal - height[l])
                maxLeft = max(maxLeft,height[l])
            else:
                r -=1
                res += max(0,minVal - height[r])
                maxRight = max(maxRight,height[r])
        return res


            

        

        


        
        
class Solution:
    def trap(self, height: List[int]) -> int:
        l,r = 0,len(height)-1
        maxL,maxR = height[l],height[r]
        res = 0
        while l<=r:
            maxL = max(maxL,height[l])
            maxR = max(maxR,height[r])
            if maxL<maxR:
                res += max(min(maxL,maxR) - height[l],0)
                l+=1
            else:
                res += max(min(maxL,maxR) - height[r],0)
                r-=1
        return res
        
        # l                  r
        # [0,2,0,3,1,0,1,3,2,1]


#         update minL,minR 
#         l<r => l+=1 else r-=1
#         l l l          r r r
#         
# min(l,r)[0]
#     l = [0,2,2,3,3,3,3,3,3,3]
#     r = [3,3,3,3,3,3,3,3,2,1]
#     res [0,0,2,0,2,3,2,0,0,0]
        
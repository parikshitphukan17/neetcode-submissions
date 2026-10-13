class Solution:
    def trap(self, height: List[int]) -> int:
        l,r = 0,len(height)-1
        maxL, maxR = height[l], height[r]
        res = 0
        while l<r:
            if maxL<maxR:
                l+=1
                maxL = max(maxL,height[l])
                res += maxL - height[l]
            else:
                r-=1
                maxR = max(maxR,height[r])
                res += maxR - height[r]
        return res






        

        # maxL = 0    2   2   3   3   3   3   3   3   3
        # maxR=  3    3   3   3   3   3   3   3   2   1

        #                 2.      2.  3.  2


        # maxL = 0
        # maxR = 1

        # if maxL<maxR:
        #     calc left
        #     new maxL
        # else
        #     calc right
        #     new maxR






    


        
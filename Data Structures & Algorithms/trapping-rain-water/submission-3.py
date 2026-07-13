class Solution:
    def trap(self, height: List[int]) -> int:
        N=len(height)
        maxL = [0]*N
        maxR = [0]*N
        maxL[0] = height[0]
        for i in range(1,N):
            maxL[i] = max(maxL[i-1],height[i])
        maxR[N-1] = height[N-1]
        for i in range(N-2,-1,-1):
            maxR[i] =max(maxR[i+1],height[i])
        

        res = 0
        for i in range(N):
            res += min(maxL[i],maxR[i]) - height[i]
        return res
        
class Solution:
    def rob(self, nums: List[int]) -> int:
        N = len(nums)
        if N<=2:
            return max(nums)
        dp = nums[N-1]
        dp2 = 0
        for i in range(N-2,0,-1):
            temp = max(dp2+nums[i],dp)
            dp2 = dp
            dp =  temp
        res = dp
        
        dp = nums[N-2]
        dp2 = 0
        for i in range(N-3,-1,-1):
            temp = max(dp2+nums[i],dp)
            dp2 = dp
            dp =  temp
        return max(res,dp)



        
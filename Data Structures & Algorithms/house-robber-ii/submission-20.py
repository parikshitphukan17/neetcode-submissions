class Solution:
    def rob(self, nums: List[int]) -> int:
        N = len(nums)
        if N<=2:
            return max(nums)
        dp = [0]*(N+1)
        dp[N-1] = nums[N-1]

        for i in range(N-2,0,-1):
            dp[i] = max(dp[i+2]+nums[i],dp[i+1])
        
        res = dp[1]
        dp = [0]*(N+1)
        dp[N-2] = nums[N-2]
        for i in range(N-3,-1,-1):
            dp[i] = max(dp[i+2]+nums[i],dp[i+1])
        return max(res,dp[0])



        
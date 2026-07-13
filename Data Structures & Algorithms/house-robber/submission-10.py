class Solution:
    def rob(self, nums: List[int]) -> int:
        N = len(nums)
        dp = [0] * (N+1)
        dp[N-1] = nums[N-1]
        for i in range(N-2,-1,-1):
            dp[i] = max(dp[i+2]+nums[i],dp[i+1])
        return dp[0]
        
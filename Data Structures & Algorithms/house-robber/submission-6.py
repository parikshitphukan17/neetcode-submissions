class Solution:
    def rob(self, nums: List[int]) -> int:
        N = len(nums)
        dp = [0] * (N+1)
        for i in range(N-1,-1,-1):
            cur = nums[i]
            if i<N-1:
                cur += dp[i+2]
            dp[i] = max(dp[i+1],cur)
        return dp[0]



        
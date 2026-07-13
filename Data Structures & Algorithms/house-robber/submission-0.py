class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = {}
        N = len(nums)
        def dfs(n):
            if n>=N:
                return 0
            if n in dp:
                return dp[n]
            dp[n] = max(nums[n]+dfs(n+2),nums[n+1]+dfs(n+3) if n+1<N else 0)
            return dp[n]
        return dfs(0)
        
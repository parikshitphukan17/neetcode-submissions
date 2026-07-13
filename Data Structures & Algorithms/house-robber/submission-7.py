class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = {}
        N = len(nums)
        def dfs(i):
            if i in dp:
                return dp[i]
            if i>=N:
                return 0
            dp[i] = max(nums[i]+dfs(i+2),dfs(i+1))
            return dp[i]
        return dfs(0)

        
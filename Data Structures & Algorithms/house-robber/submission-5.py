class Solution:
    def rob(self, nums: List[int]) -> int:
        N = len(nums)
        dp = {}
        def dfs(i):
            if i>= N:
                return 0
            if i in dp:
                return dp[i]
            dp[i] = max(nums[i] + dfs(i+2),dfs(i+1))
            return dp[i]
        return dfs(0)
        
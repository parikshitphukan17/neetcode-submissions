class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)<=2:
            return max(nums)
        N = len(nums)
        dp = {}
        def dfs(n):
            if n>=N:
                return 0
            if n in dp:
                return dp[n]
            dp[n] = max(nums[n]+dfs(n+2),nums[n+1] +dfs(n+3) if n+1<N else 0)
            return dp[n]
        val1 = dfs(1)
        N -=1
        dp = {}
        val2 = dfs(0)
        return max(val1,val2)
        
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        dp = {}
        N = len(nums)-1
        def dfs(i):
            if i in dp:
                return dp[i]
            if i>=N:
                return 0
            dp[i] = max(nums[i]+dfs(i+2),dfs(i+1))
            return dp[i]
        s = dfs(0)
        N = len(nums)
        dp = {}
        return max(s,dfs(1))
            



        
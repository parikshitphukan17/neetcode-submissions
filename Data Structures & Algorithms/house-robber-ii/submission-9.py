class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = {}
        if len(nums)<=2:
            return max(nums)
        def dfs(i,N):
            if i in dp:
                return dp[i]
            if i>=N:
                return 0
            dp[i] = max(nums[i]+dfs(i+2,N),dfs(i+1,N))
            return dp[i]
        s = dfs(0,len(nums)-1)
        dp = {}
        return max(s,dfs(1,len(nums)))
        
        
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        N = len(nums)
        
        dp = [0]*(N+2)
        for i in range(N-2,-1,-1):
            dp[i] = max(nums[i]+dp[i+2],dp[i+1])
        s = dp[0]
        dp = [0]*(N+2)
        for i in range(N-1,0,-1):
            dp[i] = max(nums[i]+dp[i+2],dp[i+1])
        return max(s,dp[1])




        # def dfs(i):
        #     if i in dp:
        #         return dp[i]
        #     if i>=N:
        #         return 0
        #     dp[i] = max(nums[i]+dfs(i+2),dfs(i+1))
        #     return dp[i]
        # s = dfs(0)
        # N = len(nums)
        # dp = {}
        # return max(s,dfs(1))
            



        
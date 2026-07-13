class Solution:
    def rob(self, nums: List[int]) -> int:
        N = len(nums)
        dp = {}
        def dfs(i):
            if i in dp:
                return dp[i]
            if i >= N:
                return 0
            dp[i] =  max(dfs(i+1),nums[i]+dfs(i+2))
            return dp[i]
        return dfs(0)
        # N = len(nums)
        # sum2 = nums[N-1]
        # sum1 = 0
        # for i in range(N-2,-1,-1):
        #     temp = max(nums[i]+sum2,sum1)
        #     sum1 = s
        #     sum2 = sum1
        # return s



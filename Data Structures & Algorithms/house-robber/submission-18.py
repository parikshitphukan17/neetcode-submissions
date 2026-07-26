class Solution:
    def rob(self, nums: List[int]) -> int:
        N = len(nums)+1
        # dp = [0]*(N)
        # dp[N-2] = nums[-1]

        sum2 = 0
        sum1 = nums[-1]
        for i in range(N-3,-1,-1):
            cur = max(nums[i]+sum2,sum1)
            sum2 = sum1
            sum1 = cur
            # dp[i] = max(nums[i]+dp[i+2],dp[i+1])
        return sum1



       

        # N = len(nums)
        # dp = {}
        # def dfs(i):
        #     if i in dp:
        #         return dp[i]
        #     if i >= N:
        #         return 0
        #     dp[i] =  max(dfs(i+1),nums[i]+dfs(i+2))
        #     return dp[i]
        # return dfs(0)
        # N = len(nums)
        # sum2 = nums[N-1]
        # sum1 = 0
        # for i in range(N-2,-1,-1):
        #     temp = max(nums[i]+sum2,sum1)
        #     sum1 = s
        #     sum2 = sum1
        # return s



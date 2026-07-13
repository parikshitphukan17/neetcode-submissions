class Solution:
    def rob(self, nums: List[int]) -> int:

        N = len(nums)
        if N<=2:
            return max(nums)
        for i in range(N-1,-1,-1):
            nc = nums[i+2] if i+2<N else 0
            nnc = nums[i+1] if i+1<N else 0
            nums[i] = max(nums[i] + nc,nnc)
        return nums[0]
        # dp = {}
        # N = len(nums)
        # def dfs(n):
        #     if n>=N:
        #         return 0
        #     if n in dp:
        #         return dp[n]
        #     dp[n] = max(nums[n]+dfs(n+2),nums[n+1]+dfs(n+3) if n+1<N else 0)
        #     return dp[n]
        # x = dfs(0)
        # print(dp)
        # return x

        
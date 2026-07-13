class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:



        N = len(nums)
        dp = [1] * N
        for i in range(N-1,-1,-1):
            for j in range(i+1,N):
                if nums[i]<nums[j]:
                    dp[i] = max(dp[i],1+dp[j])
        return max(dp)

        # def dfs(i):
        #     if i in dp:
        #         return dp[i]
        #     LIS = 1
        #     for j in range(i+1,N):
        #         if nums[i]<nums[j]:
        #             LIS = max(LIS,1+dfs(j))
        #     dp[i] = LIS
        #     return LIS
        # return max(dfs(i) for i in range(N))
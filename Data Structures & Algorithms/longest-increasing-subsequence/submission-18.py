class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        N = len(nums)
        dp =[0]*(N+1)
        for i in range(N-1,-1,-1):
            cur =[0]*(N+1)
            for j in range(i-1,-2,-1):
                cur[j] = dp[j]
                if j == -1 or nums[i]>nums[j]:
                    cur[j] = max(cur[j],1+dp[i])
            dp  = cur
        return dp[-1]
        # def dfs(i,j):
        #     if (i,j) in dp:
        #         return dp[(i,j)]
        #     if i == N:
        #         return 0
        #     LIS = dfs(i+1,j)
        #     if j == -1 or nums[i]>nums[j]:
        #         LIS = max(LIS,1+dfs(i+1,i))
        #     dp[(i,j)] = LIS
        #     return dp[(i,j)]
        # return dfs(0,-1)
            
        
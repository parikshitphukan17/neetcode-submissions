class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        M = len(nums)
        dp = [defaultdict(int) for _ in range(M+1)]
        dp[M][target] = 1
        s = sum(nums)
        for i in range(M-1,-1,-1):
            for sm in range(s,-(s+1),-1):
                dp[i][sm] = dp[i+1][sm+nums[i]] + dp[i+1][sm-nums[i]]
        return dp[0][0]


        # def dfs(i,sm):
        #     if i == M:
        #         return 1 if sm == target else 0
        #     if (i,sm) in dp:
        #         return dp[(i,sm)]
        #     dp[(i,sm)] = dfs(i+1,sm+nums[i]) + dfs(i+1,sm-nums[i])
        #     return dp[(i,sm)]
        # return dfs(0,0)

        
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        M = len(nums)
        dp = defaultdict(int)
        dp[target] = 1
        s = sum(nums)
        for i in range(M-1,-1,-1):
            cur = defaultdict(int)
            for sm in range(s,-(s+1),-1):
                cur[sm] = dp[sm+nums[i]] + dp[sm-nums[i]]
            dp = cur
        return dp[0]


        # def dfs(i,sm):
        #     if i == M:
        #         return 1 if sm == target else 0
        #     if (i,sm) in dp:
        #         return dp[(i,sm)]
        #     dp[(i,sm)] = dfs(i+1,sm+nums[i]) + dfs(i+1,sm-nums[i])
        #     return dp[(i,sm)]
        # return dfs(0,0)

        
class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0] * (n+1)
        dp[n] = 1
        for i in range(n-1,-1,-1):
            
            dp[i] = dp[i+1]
            if i<n-1:
                dp[i] += dp[i+2]
        return dp[0]
        # def climb(cur):
        #     if cur == n:
        #         return 1
        #     if cur>n:
        #         return 0
        #     if cur in dp:
        #         return dp[cur]
        #     dp[cur] = climb(cur+1) + climb(cur+2)
        #     return dp[cur]
        # return climb(0)

        
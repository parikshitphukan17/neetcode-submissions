class Solution:
    def climbStairs(self, n: int) -> int:
        dp = {}
        def climb(cur):
            if cur == n:
                return 1
            if cur>n:
                return 0
            if cur in dp:
                return dp[cur]
            dp[cur] = climb(cur+1) + climb(cur+2)
            return dp[cur]
        return climb(0)

        
class Solution:
    def integerBreak(self, n: int) -> int:
        dp = {1:1}
        def dfs(num):
            if num in dp:
                return dp[num]
            res = 0
            for i in range(1,num):
                res = max(res,i * (num-i),i*dfs(num-i))
            dp[num] = res
            return res
        return dfs(n)

            
            
        
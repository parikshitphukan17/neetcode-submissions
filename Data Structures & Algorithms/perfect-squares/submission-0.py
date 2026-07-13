class Solution:
    def numSquares(self, n: int) -> int:

        dp = {}
        def dfs(target):
            if target == 0:
                return 0
            if target in dp:
                return dp[target]
            res = target

            for i in range(1,target):
                if i*i>target:
                    break
                res = min(res,1+dfs(target - (i*i)))
            dp[target] = res
            return res
        return dfs(n)


        # 13
        # 1-> 1 + 1 + 1 + 3 
        # dp[1] = 1
        # dp[2] = 2
        # dp[3] =3
        # dp[4] = 1
        # dp[5] = 2
        # dp[6] = 2
        # dp[7] = 3
        # dp[8]

        
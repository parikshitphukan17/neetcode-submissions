class Solution:
    def integerBreak(self, n: int) -> int:
        dp = {}
        def dfs(number,prod):
            if number == 0:
                return prod
            if (number,prod) in dp:
                return dp[(number,prod)]
            res = 0
            for i in range(1,number+1):
                if i ==n:
                    break
                res = max(res,dfs(number-i,prod*i))
            dp[(number,prod)] = res
            return res
        return dfs(n,1)

            
            
        
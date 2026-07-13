class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = {}
        def dfs(amt):
            if amt == 0:
                return 0
            if amt in dp:
                return dp[amt]
            res = 10**9 +7
            for c in coins:
                if amt-c>=0:
                    res = min(res,1+dfs(amt-c))
            dp[amt] = res
            return dp[amt]
        res = dfs(amount)
        return -1 if res>amount  else res
        
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        N = len(coins)
        dp ={}
        def dfs(i,amt):
            if (i,amt) in dp:
                return dp[(i,amt)]
            if i == N or amt>amount:
                return 0
            if amt == amount:
                return 1
            dp[(i,amt)] = dfs(i,amt+coins[i]) + dfs(i+1,amt)
            return dp[(i,amt)]
        return dfs(0,0)
        
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        M = len(coins)
        dp = [0]* (amount+1)
        for i in range(M-1,-1,-1):
            cur = [0]* (amount+1)
            for j in range(amount,-1,-1):
                if j == amount:
                    cur[j] = 1
                else:
                    cur[j] = dp[j] + (cur[j+coins[i]] if j+coins[i]<=amount else 0)
            dp = cur
        return dp[0]
        # def dfs(i,amt):
        #     if i == M or amt>amount:
        #         return 0
        #     if (i,amt) in dp:
        #         return dp[(i,amt)]
        #     if amt == amount:
        #         return 1
        #     dp[(i,amt)] = dfs(i,amt + coins[i]) + dfs(i+1,amt)
        #     return dp[(i,amt)]
        # return dfs(0,0)
            

        
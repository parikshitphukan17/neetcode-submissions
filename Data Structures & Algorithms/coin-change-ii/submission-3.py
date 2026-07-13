class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        N = len(coins)
        dp = {}
        def dfs(i,sm):
            if sm == amount:
                return 1

            if i == N or sm > amount:
                return 0
            if (i,sm) in dp:
                return dp[(i,sm)]
            dp[(i,sm)] = dfs(i+1,sm) + dfs(i,sm+coins[i])
            return dp[(i,sm)]
        return dfs(0,0)

        
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = {}
        def dfs(i,sm):
            if (i,sm) in dp:
                return dp[(i,sm)]
            if sm>amount or i>= len(coins):
                return 0
            if sm == amount:
                return 1
            dp[(i,sm)] =  dfs(i,sm+coins[i]) + dfs(i+1,sm)
            return dp[(i,sm)]
        return dfs(0,0)
        
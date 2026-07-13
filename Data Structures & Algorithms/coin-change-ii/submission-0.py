class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = {}
        def dfs(i,sm):
            if (i,sm) in dp:
                return dp[(i,sm)]
            if i== len(coins) or sm>amount:
                dp[(i,sm)] = 0
            elif sm == amount:
                dp[(i,sm)] = 1
            else:
                dp[(i,sm)] = dfs(i,sm+coins[i]) + dfs(i+1,sm)
            return dp[(i,sm)]
        return dfs(0,0)
                
        
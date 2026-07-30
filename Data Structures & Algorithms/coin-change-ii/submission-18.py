class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        res = 0
        dp = {}
        N = len(coins)
        def dfs(i,cur):
            if cur == amount:
                return 1
            nonlocal res
            if i==N or cur>amount:
                return 0
            if (i,cur) in dp:
                return dp[(i,cur)]
            dp[(i,cur)] = dfs(i,cur+coins[i]) + dfs(i+1,cur)
            return dp[(i,cur)]

        return dfs(0,0)
            
        
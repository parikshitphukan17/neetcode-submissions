class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        coins.sort()
        N = len(coins)
        dp = {}
        def dfs(i,cur):
            if cur == amount:
                return 1
            if i == N or cur > amount:
                return 0
            if (i,cur) in dp:
                return dp[(i,cur)]
            
            dp[(i,cur)] = dfs(i+1,cur) + dfs(i,cur+coins[i])
            return dp[(i,cur)]
        return dfs(0,0)

        
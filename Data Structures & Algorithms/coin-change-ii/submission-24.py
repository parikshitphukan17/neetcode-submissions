class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        N = len(coins)
        dp = {}
        def dfs(i,cur):
            if cur>=amount:
                return 1 if cur==amount else 0
            if i ==N:
                return 0
            if (i,cur) in dp:
                return dp[(i,cur)]
            dp[(i,cur)] = dfs(i,cur+coins[i]) + dfs(i+1,cur)
            return dp[(i,cur)]
        return dfs(0,0)
            
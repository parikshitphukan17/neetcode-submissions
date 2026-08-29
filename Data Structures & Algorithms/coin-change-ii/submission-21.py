class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        N = len(coins)
        dp = {}
        def dfs(i,s):
            if s == amount:
                return 1
            if s>amount or i == N:
                return 0
            if (i,s) in dp:
                return dp[(i,s)]
            dp[(i,s)] = dfs(i,s+coins[i])+dfs(i+1,s)
            return dp[(i,s)]
        return dfs(0,0)

        #                                                                     0,0
        #                                     1,0 (3)                                     0,1
        #                 2,0 (2)                                 1,1(1)                 2,1(1)             0,2
        #         3,0(1)                  2,1(1)            3,1  X        1,2 (1)                    3,2
        # 4,0             3,1        4,1      2,2X                     4,2
        #                 X,4,1X
       

        
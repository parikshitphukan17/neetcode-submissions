class Solution:
    def numDecodings(self, s: str) -> int:
        dp = {}
        N = len(s)
        def dfs(i):
            if i in dp:
                return dp[i]
            if i>=N:
                return 1 if i == N else 0
            if s[i] == "0":
                return 0
            double = 0 if (i+1>=N or int(s[i:i+2]) > 26) else dfs(i+2)
            dp[i] = dfs(i+1)+double
            return dp[i]
        return dfs(0)


        # f
        # 1012
        # if i in dp:
        #     return dp[i]
        # if i == N:
        #     return 1
        # if i>N:
        #     return 0
        # dp[i] = {take i if not 0 
        # take i+1 if not s[i:i+2] <=26}
        
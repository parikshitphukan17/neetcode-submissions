class Solution:
    def numDecodings(self, s: str) -> int:
        dp = {}
        N = len(s)
        def dfs(i):
            if i == N:
                return 1
            if i>N:
                return 0
            if s[i] =="0":
                return 0
            if i in dp:
                return dp[i]
            cur = dfs(i+1)
            nxt = 0
            if i+1<N:
                if int(s[i:i+2]) in range(1,27):
                    nxt = dfs(i+2)
            dp[i] =  cur+nxt
            return dp[i]
        return dfs(0)

        
class Solution:
    def numDecodings(self, s: str) -> int:
        N = len(s)
        dp = [0]*(N+1)
        dp[N] = 1
        # def dfs(i):
        #     if i ==N:
        #         return 1
        #     if s[i] == "0":
        #         return 0
        #     if i in dp:
        #         return dp[i]
        #     dp[i] = dfs(i+1) + (dfs(i+2) if (i+1<N and 0<int(s[i:i+2])<=26)else 0)
        #     return dp[i]
        for i in range(N-1,-1,-1):
            if s[i] == "0":
                continue
            dp[i] = dp[i+1] + (dp[i+2] if (i+1<N and 0<int(s[i:i+2])<=26)else 0)
        return dp[0]

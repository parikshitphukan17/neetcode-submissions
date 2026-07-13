class Solution:
    def numDecodings(self, s: str) -> int:
        N = len(s)
        # def dfs(i):
        #     if i ==N:
        #         return 1
        #     if s[i] == "0":
        #         return 0
        #     if i in dp:
        #         return dp[i]
        #     dp[i] = dfs(i+1) + (dfs(i+2) if (i+1<N and 0<int(s[i:i+2])<=26)else 0)
        #     return dp[i]
        n1,n2 = 1,0
        for i in range(N-1,-1,-1):
            if s[i] == "0":
                cur = 0
            else:
                cur = n1 + (n2 if (i+1<N and 0<int(s[i:i+2])<=26)else 0)
            n1,n2 = cur,n1

        return n1

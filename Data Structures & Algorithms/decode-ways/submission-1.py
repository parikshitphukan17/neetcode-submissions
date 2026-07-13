class Solution:
    def numDecodings(self, s: str) -> int:
        N = len(s)
        dp = [0] * (N+1)
        dp[N] = 1
        for i in range(N-1,-1,-1):
            if s[i] == "0":
                continue
            nxt = dp[i+2] if i+1<N and int(s[i:i+2]) in range(1,27) else 0
            dp[i] = dp[i+1] +nxt
        return dp[0]

            

        
        # def dfs(i):
        #     if i == N:
        #         return 1
        #     if i>N:
        #         return 0
        #     if s[i] =="0":
        #         return 0
        #     if i in dp:
        #         return dp[i]
        #     cur = dfs(i+1)
        #     nxt = 0
        #     if i+1<N:
        #         if int(s[i:i+2]) in range(1,27):
        #             nxt = dfs(i+2)
        #     dp[i] =  cur+nxt
        #     return dp[i]
        # return dfs(0)

        
class Solution:
    def numDecodings(self, s: str) -> int:
        dp = {}
        N = len(s)
        def dfs(i):
            if i in dp:
                return dp[i]
            if i == N:
                return 1
            if i >N:
                return 0
            if s[i] == "0":
                return 0
            if i+1<N and int(s[i:i+2]) in range(1,27):
                dp[i] = dfs(i+1) + dfs(i+2)
            else:
                dp[i] = dfs(i+1)
            return dp[i]
        return dfs(0)
            
            



        # 226
        # BBF
        # BV

        
class Solution:
    def numDecodings(self, s: str) -> int:
        N = len(s)
        sum1 = 1
        sum2 = 0
        for i in range(N-1,-1,-1):
            if s[i] == "0":
                cur = 0
            else:
                cur = sum1
                if i+1<N and int(s[i:i+2])<=26:
                    cur += sum2
            sum2 = sum1
            sum1 = cur
        return sum1

        # def dfs(i):
        #     if i ==N:
        #         return 1
        #     if i in dp:
        #         return dp[i]
        #     if s[i] == "0":
        #         return 0
        #     if i+1<N and int(s[i:i+2])<=26:
        #         dp[i] = dfs(i+1)+dfs(i+2)
        #     else:
        #         dp[i] = dfs(i+1)
        #     return dp[i]
        # return dfs(0)
            

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        M,N = len(s), len(t)
        dp = [0]*(N+1)
        dp[N] = 1
        for i in range(M-1,-1,-1):
            cur = [0]*(N+1)
            cur[N] = 1
            for j in range(N-1,-1,-1):
                if s[i] == t[j]:
                    cur[j] = dp[j+1] + dp[j]
                else:
                    cur[j] = dp[j]
            dp = cur
        return cur[0]

        
      
        
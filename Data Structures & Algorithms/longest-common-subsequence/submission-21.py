class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        M,N = len(text1),len(text2)
        dp = [0]*(N+1)
        for i in range(M-1,-1,-1):
            cur = [0]*(N+1)
            for j in range(N-1,-1,-1):
                if text1[i] == text2[j]:
                    cur[j] = 1 + dp[j+1]
                else:
                    cur[j] = max(dp[j],cur[j+1])
            dp = cur
        return dp[0]
                    


            
        



       
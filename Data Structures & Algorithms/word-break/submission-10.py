class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        N = len(s)
        dp = [False]*(N+1)
        dp[len(s)] = True
        for i in range(N-1,-1,-1):
            for w in wordDict:
                if dp[i]:
                    break
                if i+len(w)<=N and s[i:i+len(w)] == w:
                    dp[i] = dp[i+len(w)]
        return dp[0]
                


        
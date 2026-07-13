class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = {}
        N = len(s)
        def dfs(i):
            if i == N:
                return True
            if i in dp:
                return dp[i]
            for w in wordDict:
                if i+len(w)<=N and s[i:i+len(w)] == w:
                    dp[i] = dfs(i+len(w))
                    if dp[i]:
                        return dp[i]
            dp[i] = False
            return dp[i]
        return dfs(0)


        
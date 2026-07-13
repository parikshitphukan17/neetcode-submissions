class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        N = len(s)
        dp = {}
        def dfs(i):
            if i in dp:
                return dp[i]
            if i == N:
                return True
            for w in wordDict:
                if i + len(w) <=N and s[i:i+len(w)] == w:
                    if dfs(i+len(w)):
                        dp[i] = True
                        return dp[i]
            dp[i] =  False
            return dp[i]
        return dfs(0)


        
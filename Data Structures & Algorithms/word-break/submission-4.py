class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        N = len(s)
        dp = {}
        def dfs(i):
            if i == N:
                return True
            if i in dp:
                return dp[i]
            for word in wordDict:
                if i+len(word)-1<N and s[i:i+len(word)] == word:
                    if dfs(i+len(word)):
                        dp[i] = True
                        return True
            dp[i] =  False
            return dp[i]
        return dfs(0)

        
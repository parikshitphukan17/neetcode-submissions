class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        N = len(s)
        dp = [False] * (N+1)
        dp[N] = True
        for i in range(N-1,-1,-1):
            for w in wordDict:
                if i+len(w)-1<N and s[i:i+len(w)] == w:
                    if dp[i+len(w)] == True:
                        dp[i] = True
                        break
        return dp[0]
        # def dfs(i):
        #     if i == N:
        #         return True
        #     if i in dp:
        #         return dp[i]
        #     for word in wordDict:
        #         if i+len(word)-1<N and s[i:i+len(word)] == word:
        #             if dfs(i+len(word)):
        #                 dp[i] = True
        #                 return True
        #     dp[i] =  False
        #     return dp[i]
        # return dfs(0)

        
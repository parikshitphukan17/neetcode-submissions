class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        N = len(s)
        dp = [False]*(N+1)
        dp[N] = True
        for i in range(N-1,-1,-1):
            for w in wordDict:
                if dp[i]:
                    break
                if i+len(w)<=N and w == s[i:i+len(w)]:
                    dp[i] = dp[i+len(w)]
        return dp[0]
        # def dfs(i):
        #     if i ==N:
        #         return True
        #     if i in vis:
        #         return False
        #     for w in wordDict:
        #         if i+len(w)<=N and w == s[i:i+len(w)] and dfs(i+len(w)):
        #             return True
        #     vis.add(i)
        #     return False
        # return dfs(0)



        # N = len(s)
        # dp = [False]*(N+1)
        # dp[N] = True
        # for i in range(N-1,-1,-1):
        #     for w in wordDict:
        #         if dp[i]:
        #             break
        #         if i+len(w)<=N and s[i:i+len(w)] == w:
        #             dp[i] = dp[i+len(w)]
        # return dp[0]
        
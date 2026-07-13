class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        N = len(s)
        dp = set()
        def dfs(i):
            if i == N:
                return True
            if i in dp:
                return False
            for w in wordDict:
                if i+len(w)<=N and s[i:i+len(w)] == w and dfs(i+len(w)):
                    return True
            dp.add(i)
            return False
        return dfs(0)

        
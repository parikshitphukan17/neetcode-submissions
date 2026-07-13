class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = set()
        def dfs(i):
            if i in dp:
                return False
            if i == len(s):
                return True
            if i>len(s):
                return False
            for w in wordDict:
                if i + len(w) -1<len(s):
                    if dfs(i+len(w)) and s[i:i+len(w)] == w:
                        return True
            dp.add(i)
            return False
        return dfs(0)

        
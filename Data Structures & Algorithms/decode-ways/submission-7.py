class Solution:
    def numDecodings(self, s: str) -> int:
        N = len(s)
        def dfs(i):
            if i ==N:
                return 1
            if s[i] == "0":
                return 0
            return dfs(i+1) + (dfs(i+2) if (i+1<N and 0<int(s[i:i+2])<=26)else 0)
        return dfs(0)


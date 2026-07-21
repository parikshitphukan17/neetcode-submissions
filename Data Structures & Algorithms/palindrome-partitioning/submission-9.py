class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        def dfs(cur,s):
            if not s:
                res.append(cur.copy())
            for i in range(len(s)):
                sub = s[:i+1]
                if sub!= sub[::-1]:
                    continue
                cur.append(sub)
                dfs(cur,s[i+1:])
                cur.pop()
        dfs([],s)
        return res
        
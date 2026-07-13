class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        def dfs(cur,s):
            if not s:
                res.append(cur.copy())
            
            for i in range(len(s)):
                w = s[:i+1]
                if w == w[::-1]:
                    cur.append(w)
                    dfs(cur,s[i+1:])
                    cur.pop()
        dfs([],s)
        return res
                




        
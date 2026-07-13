class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def dfs(s,cur):
            if not s:
                res.append(cur.copy())
                return
            for i in range(len(s)):
                word = s[:i+1]
                if word == word[::-1]:
                    cur.append(word)
                    dfs(s[i+1:],cur)
                    cur.pop()
        dfs(s,[])
        return res




        # aab
        # a.   ab 
        # aa.      b

        
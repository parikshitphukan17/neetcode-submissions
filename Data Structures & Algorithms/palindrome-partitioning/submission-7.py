class Solution:
    def partition(self, s: str) -> List[List[str]]:

        res = []
        def dfs(sub,cur):
            if not sub:
                res.append(cur.copy())
                return
            for i in range(len(sub)):
                text = sub[:i+1]
                if text == text[::-1]:
                    cur.append(text)
                    dfs(sub[i+1:],cur)
                    cur.pop()
        dfs(s,[])
        return res



        # aab
        # a   a   b
        # aa  b
        
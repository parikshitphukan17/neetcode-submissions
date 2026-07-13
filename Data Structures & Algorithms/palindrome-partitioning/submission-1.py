class Solution:
    def partition(self, s: str) -> List[List[str]]:
        l = len(s)
        self.res = []
        def dfs(i,cur):
            if i==l:
                self.res.append(cur.copy())
                return
            for j in range(1,l-i+1):
                w = s[i:i+j]
                if w == w[::-1]:
                    cur.append(w)
                    dfs(i+j,cur)
                    cur.pop()
        dfs(0,[])
        return self.res


        
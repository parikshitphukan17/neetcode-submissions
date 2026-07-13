class Solution:
    def partition(self, s: str) -> List[List[str]]:
        cur,res = [],[]
        def dfs(sub):
            if not sub:
                res.append(cur.copy())
                return
            for i in range(len(sub)):
                curS = sub[:i+1]
                if curS == curS[::-1]:
                    cur.append(curS)
                    dfs(sub[i+1:])
                    cur.pop()
        dfs(s)
        return res
        
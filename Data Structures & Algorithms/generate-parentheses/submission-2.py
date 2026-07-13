class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def dfs(o,c,cur):
            if o==n and c==n:
                res.append("".join(cur))
                return
            if c>o:
                return
            if o<n:
                cur.append("(")
                dfs(o+1,c,cur)
                cur.pop()
            if c<n:
                cur.append(")")
                dfs(o,c+1,cur)
                cur.pop()
        dfs(0,0,[])
        return res
        
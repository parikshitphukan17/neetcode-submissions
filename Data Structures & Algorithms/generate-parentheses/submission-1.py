class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def dfs(op,cl,cur):
            if op == n and cl == n:
                res.append("".join(cur))
                return
            if cl>op:
                return
            if op<n:
                cur.append("(")
                dfs(op+1,cl,cur)
                cur.pop()
            if cl<n:
                cur.append(")")
                dfs(op,cl+1,cur)
                cur.pop()
        dfs(0,0,[])
        return res
        
            
                
        
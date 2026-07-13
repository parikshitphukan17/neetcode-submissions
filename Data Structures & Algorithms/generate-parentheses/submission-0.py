class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def dfs(op,cl,brack):
            if cl<op or op<0 or cl<0:
                return
            if op == 0 and cl ==0:
                res.append(str(brack))
                return
            dfs(op-1,cl,brack+"(")
            dfs(op,cl-1,brack+")")
        dfs(n,n,"")
        return res


        
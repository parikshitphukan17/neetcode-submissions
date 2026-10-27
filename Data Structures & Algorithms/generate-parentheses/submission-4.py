class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def dfs(string,o,c):
            nonlocal n
            if o == n and c == n:
                res.append(string)
                return
            if o==n:
                dfs(string+")",o,c+1)
                return
            elif o==c:
                dfs(string+"(",o+1,c)
                return
            if o>c:
                dfs(string+"(",o+1,c)
                dfs(string+")",o,c+1)
        dfs("",0,0)
        return res
            
        
                



        
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        N,M = len(s),len(p)
        dp = {}

        def dfs(i,j):
            if i == N:
                if j == M:
                    return True
                if p[j] == '*':
                    return dfs(i,j+1)
                if j+1 <M and p[j+1] == '*':
                    return dfs(i,j+2)
                return False
            if j== M:
                return False
            if (i,j) in dp:
                return dp[(i,j)]
            if s[i] == p[j] or p[j] == '.':
                dp[(i,j)] = dfs(i+1,j+1)
            elif p[j] == '*':
                if s[i] == p[j-1] or p[j-1] == '.':
                    dp[(i,j)] = dfs(i+1,j+1) or dfs(i+1,j) or dfs(i,j+1)
                else:
                    dp[(i,j)] = dfs(i,j+1)
            else:
                if j+1 <M and p[j+1] == "*":
                    dp[(i,j)] = dfs(i,j+2)
                else:
                    dp[(i,j)] = False
            return dp[(i,j)]
        return dfs(0,0)


            

        
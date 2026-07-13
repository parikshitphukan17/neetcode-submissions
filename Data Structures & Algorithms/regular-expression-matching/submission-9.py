class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        N,M =len(s),len(p)
        dp = {}
        def dfs(i,j):
            if j==M:
                return i == N
            if (i,j) in dp:
                return dp[(i,j)]
            m = i<N and (s[i] == p[j] or p[j] == ".")
            if j+1<M and p[j+1] == "*":
                dp[(i,j)] = (m and dfs(i+1,j)) or dfs(i,j+2)
            elif m:
                dp[(i,j)] = dfs(i+1,j+1)
            else:
                dp[(i,j)] = False
            return dp[(i,j)]
        return dfs(0,0)




        # nnn .*
        # i.   
        # j
        


        
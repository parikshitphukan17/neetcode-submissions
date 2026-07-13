class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        N,M =len(s),len(p)
        def dfs(i,j):
            if j==M:
                return i == N
            m = i<N and (s[i] == p[j] or p[j] == ".")
            if j+1<M and p[j+1] == "*":
                return (m and dfs(i+1,j)) or dfs(i,j+2)
            elif m:
                return dfs(i+1,j+1)
            else:
                return False
        return dfs(0,0)




        # nnn .*
        # i.   
        # j
        


        
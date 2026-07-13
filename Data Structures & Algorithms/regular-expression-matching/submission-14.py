class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = {}
        M,N = len(s), len(p)
        def dfs(i,j):
            print(i,j)
            if i == M and j == N:
                return True
            if j ==N:
                return False
            if (i,j) in dp:
                return dp[(i,j)]
            isMatch = i<M and (s[i] == p[j] or p[j] == ".")
            if j+1<N and p[j+1] == "*":
                dp[(i,j)] = (isMatch and dfs(i+1,j)) or dfs(i,j+2)
            elif isMatch:
                dp[(i,j)] = dfs(i+1,j+1)
            else:
                dp[(i,j)] = False
            return dp[(i,j)]
        return dfs(0,0)




        
        # i.     j 
        # abcd   .*

        # if i == len(s) and j == len(p):
        #     return True
        
        # if j+1 == "*":
            
        
        # elif isMatch
        
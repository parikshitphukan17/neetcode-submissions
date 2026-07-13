class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:


        dp = {}
        N = len(s3)
        M = len(s1)
        L = len(s2)
        if N!= M+L:
            return False
        def dfs(i,j,k):
            if k== N:
                return True
            if (i,j) in dp:
                return dp[(i,j)]
            canIReach = False
            if i<M and s1[i] == s3[k]:
                canIReach = dfs(i+1,j,k+1)
            canJReach = False
            if j<L and s2[j] == s3[k]:
                canJReach =  dfs(i,j+1,k+1)
            dp[(i,j)] = canIReach or canJReach
            return dp[(i,j)]
        return dfs(0,0,0)







        
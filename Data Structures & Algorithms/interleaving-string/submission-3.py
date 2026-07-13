class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        N,M,K = len(s1),len(s2),len(s3)
        if N+M != len(s3):
            return False
        dp = {}
        def dfs(i,j,k):
            if k == K:
                return i==N and j == M
            if (i,j) in dp:
                return dp[(i,j)]
            res = False
            if i<N and s1[i] == s3[k]:
                res = dfs(i+1,j,k+1)
                if res:
                    return res
            if j<M and s2[j] == s3[k]:
                res = dfs(i,j+1,k+1)
                if res:
                    return res
            
            dp[(i,j)] =  res
            return dp[(i,j)]
        return dfs(0,0,0)

            
            

        
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        N,M,K = len(s1),len(s2),len(s3)
        if N+M != len(s3):
            return False
        def dfs(i,j,k):
            if k == K:
                return i==N and j == M
            if i<N and s1[i] == s3[k] and dfs(i+1,j,k+1):
                return True
            if j<M and s2[j] == s3[k] and dfs(i,j+1,k+1):
                return True
            return False
        return dfs(0,0,0)

            
            

        
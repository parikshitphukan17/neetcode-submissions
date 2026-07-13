class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) +len(s2) != len(s3):
            return False
        if abs(len(s1)-len(s2))>1:
            return False
        N,M,K = len(s1),len(s2),len(s3) 
        dp = set()
        def dfs(i,j,k):
            if k == K:
                return i ==N and j == M
            if (i,j) in dp:
                return False
            if i<N and s1[i] == s3[k]:
                if dfs(i+1,j,k+1):
                    return True
            if j<M and s2[j] == s3[k]:
                if dfs(i,j+1,k+1):
                    return True
            dp.add((i,j))
            return False
        return dfs(0,0,0)
        
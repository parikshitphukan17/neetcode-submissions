class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        N,M,K = len(s1),len(s2),len(s3)
        dp = {}
        def dfs(i,j,k):
            if k==K:
                return N == i and j == M
            if (i,j) in dp:
                return dp[(i,j)]
            if i<N and s1[i] == s3[k] and dfs(i+1,j,k+1):
                dp[(i,j)] = True
            elif j<M and s2[j] == s3[k] and dfs(i,j+1,k+1):
                dp[(i,j)] = True
            else:
                dp[(i,j)] = False
            return dp[(i,j)]
        return dfs(0,0,0)
            
            




        # 0.   0
        # aaaa bbbb

        # aaab

        # aabbbbaa
        # 0
        
        # i+1,j
        # i,j+1
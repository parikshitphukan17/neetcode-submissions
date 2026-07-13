class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:

        N,M,K = len(s1),len(s2),len(s3)
        dp = {}
        def dfs(i,j,k,last,c1,c2):
            if k == K:
                return i==N and j==M and abs(c2-c1)<=1
            key = (i,j,k,last,c1,c2)
            if key in dp:
                return dp[key]
            dp[key] = False
            if i<N and s1[i] == s3[k]:
                if last == 1 and dfs(i+1,j,k+1,1,c1,c2):
                    dp[key] = True
                elif last != 1 and dfs(i+1,j,k+1,1,c1+1,c2):
                    dp[key] = True

            if j<M and s2[j] == s3[k]:
                if last == 2 and dfs(i,j+1,k+1,2,c1,c2):
                    dp[key] = True
                    
                elif last !=2 and dfs(i,j+1,k+1,2,c1,c2+1):
                    dp[key] =True
               
            return dp[key]
        return dfs(0,0,0,0,0,0)

        # aaaa bbbb. aabbbbaa
        # i    j
        # if i == k:
        #    if true i+1,j return true
        # if j==k:
        #     if true i,j+1 return True
        

        
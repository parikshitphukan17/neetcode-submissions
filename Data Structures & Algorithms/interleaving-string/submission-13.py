class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        M,N,K  = len(s1),len(s2),len(s3)
        if M+N != K:
            return False
        dp = [[False]*(N+1) for _ in range(M+1)]
        dp[M][N] = True
        for i in range(M,-1,-1):
            for j in range(N,-1,-1):
                k = i+j
                if k == K or dp[i][j]:
                    continue
                if i<M and s1[i] == s3[k] and dp[i+1][j]:
                    dp[i][j] = dp[i+1][j]
                if j<N and s2[j] == s3[k] and dp[i][j+1]:
                    dp[i][j] = dp[i][j+1]
        return dp[0][0]


                
                
        # def dfs(i,j):
        #     k = i+j
        #     if k == K:
        #         return True
        #     if (i,j) in vis:
        #         return False
        #     if i<M and s1[i] == s3[k]:
        #         if dfs(i+1,j):
        #             return True
        #     if j<N and s2[j] == s3[k]:
        #         if dfs(i,j+1):
        #             return True
        #     vis.add((i,j))
        #     return False
        # return dfs(0,0)
    #     i
    #     a   a   a   a           
    #     j
    #     b   b   b   b
    #     k
    #     a   a   b   b   b   b   a   a
    #     k= i+j
    #     check if i == k? yes go to next
    #     no check for j==k? 
    #     no return False

    # i   0   1   2   3   4
    #     a   a   a   a   
    # j   0   1   2   3   4
    #     b   b   b   b
    

        
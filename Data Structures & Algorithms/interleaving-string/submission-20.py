class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:

    # i   0   1   2   3           j   0   1   2   3
    #     a   a   a   a               b   b   b   b

    # k   0   1   2   3   4   5   6   7
    #     a   a   b   b   b   b   a   a
        M,N,O= len(s1),len(s2),len(s3)
        if M+N != O:
            return False
        dp = {}
        def dfs(i,j):
            k =i+j
            if k == O:
                return True
            if (i,j) in dp:
                return dp[(i,j)]
            if i<M and s1[i]== s3[k] and dfs(i+1,j):
                return True
            if j<N and s2[j] == s3[k] and dfs(i,j+1):
                return True
            dp[(i,j)] = False
            return False
        return dfs(0,0)




        
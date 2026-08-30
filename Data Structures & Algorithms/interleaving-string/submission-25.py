class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        M,N,K = len(s1),len(s2),len(s3)
        if M+N != K:
            return False
        vis = set()
        def dfs(i,j):
            k = i+j
            if (i,j) in vis:
                return False
            if k == K:
                return True
            if i<M and s1[i] == s3[k] and dfs(i+1,j):
                return True
            if j<N and s2[j] == s3[k] and dfs(i,j+1):
                return True
            vis.add((i,j))
            return False
        return dfs(0,0)



        # 0
        # i
        # a   a   a   a
        
        # 0
        # j
        # b   b   b   b

        # k= i+j
        # 0
        # k
        # a   a   b   b   b   b   a   a   



        
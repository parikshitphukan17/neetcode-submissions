class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = {}
        M,N = len(word1),len(word2)
        def dfs(i,j):
            if (i,j) in dp:
                return dp[(i,j)]
            if i == M and j ==N:
                return 0
            if i== M:
                dp[(i,j)] = 1 + dfs(i,j+1)
            elif j == N:
                dp[(i,j)] = 1 + dfs(i+1,j)
            elif word1[i] == word2[j]:
                dp[(i,j)] = dfs(i+1,j+1)
            else:
                dp[(i,j)] = 1 +min(dfs(i,j+1),dfs(i+1,j),dfs(i+1,j+1))
            return dp[(i,j)]
        return dfs(0,0)







        #       i
        # m o n k e y s
        #       j
        # m o n e y
        # i == j ->. (i+1,j+1)
        # i!=j.  1 + min(insert(i,j+1), delete(i+1,j), rep(i+1,j+1))

        # i == N and j == M:
        #     return 0
        # i == N:
        #    1 + insert(i,j+1)
        
        # j == M:
        #     i<N:
        #     1 + delete(i+1,j)
            

        
class Solution:
    def numDecodings(self, s: str) -> int:
        N = len(s)

        def dfs(i):
            if i ==N:
                return 1
            if i>N:
                return 0
            if s[i] == "0":
                return 0
            if i+1<N and int(s[i:i+2]) in range(1,27):
                return dfs(i+1) + dfs(i+2)
            return dfs(i+1)
        return dfs(0)
            



        # if i== 0
        #     return 0
        # if i+1<N:
        #     if int(s[i:i+2]) in range(1,27)





        
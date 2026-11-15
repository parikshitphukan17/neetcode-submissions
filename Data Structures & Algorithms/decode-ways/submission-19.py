class Solution:
    def numDecodings(self, s: str) -> int:
        N = len(s)
        dp = 1
        dp2 = 0
        for i in range(N-1,-1,-1):
            res = 0
            if s[i] != "0":
                res = dp
                if i+1<N and int(s[i:i+2])<=26:
                    res += dp2
            dp2 = dp
            dp = res
        return dp
                
       
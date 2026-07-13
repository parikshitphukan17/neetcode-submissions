class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l,r = 0,0
        N = len(s)
        dp = {}
        res = 0
        while r<N:
            if s[r] in dp:
                l = max(l,dp[s[r]]+1)
            dp[s[r]] = r
            res = max(res,r-l+1)
            r+=1
        return res




        #     i   i   j.  j
        # z   x   y   z   x   y   z


        # when encounter exisitng val change l to max(l,prev+1)
           
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dp ={}
        l,r = 0,0
        res = 0
        while r<len(s):
            if s[r] in dp:
                l = max(l,dp[s[r]]+1)
            dp[s[r]] = r
            res = max(r-l+1,res)
            r+=1
        return res



class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        l,r = 0,0
        pos = {}
        res = 0
        while r<len(s):
            if s[r] in pos:
                l = max(l,pos[s[r]]+1)
            pos[s[r]] = r
            res = max(res,r-l+1)
            r+=1
        return res

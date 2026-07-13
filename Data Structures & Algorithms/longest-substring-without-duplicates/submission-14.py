class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        smap = {}
        l,r = 0,0
        res = 0
        while r<len(s):
            if s[r] in smap:
                l = max(l,smap[s[r]] +1)
            smap[s[r]] = r
            res = max(res,r-l+1)
            r+=1
        return res

        
        
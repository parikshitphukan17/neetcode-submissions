class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        smap = {}
        res = 0
        for r in range(len(s)):
            if s[r] in smap:
                l = max(l,smap[s[r]]+1)
            res = max(res,r-l+1)
            smap[s[r]] = r
        return res
            

            


    #     zxyzxyz

    #     zxyzyxz
    # l = 0,1,1,3,3,4
    # i = 3,3,4,4,5,6
        
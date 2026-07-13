class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        vis,l,res = {},0,0
        for i in range(len(s)):
            c =s[i]
            if c in vis:
                l = max(l,vis[c]+1)
            res = max(res,i-l+1)
            vis[c] = i
        return res
        
        
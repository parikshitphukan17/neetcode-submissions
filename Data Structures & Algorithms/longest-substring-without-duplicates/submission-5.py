class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        pos,i,j,res = {},0,0,0
        while j<len(s):
            if s[j] in pos:
                i = max(pos[s[j]]+1,i)
            pos[s[j]] = j
            res = max(res,j-i+1)
            j+=1
        return res
        
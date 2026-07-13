class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l,i = 0,0
        smap = {}
        res = 0
        while i<len(s):
            if s[i] in smap:
                print(l,i)
                res = max(res,i-l)
                l = smap[s[i]]+1
                smap = {}
                for j in range(l,i):
                    smap[s[j]] = j
            smap[s[i]] = i
            i+=1
        return max(res,i-l)




    #     i = 0
    #     res = 0
    #     dvdf
    # i.  0
    # j.  0
    #     while i <len(s):
    #         if i in map:
    #             res = max(i-s,res)
    #             i = map[i]+1

#     abba
# l.  0.2
# i.  0123
            




        
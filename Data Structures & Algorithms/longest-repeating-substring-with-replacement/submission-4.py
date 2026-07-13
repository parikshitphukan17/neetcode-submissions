class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l,r = 0,0
        maxF = 0
        smap = defaultdict(int)
        res = 0
        while r<len(s):
            smap[s[r]] = smap[s[r]]+1
            maxF = max(maxF,smap[s[r]])
            while r-l-maxF+1>k:
                smap[s[l]] -=1
                l+=1
            res = max(res,r-l+1)
            r+=1
        return res

        #  ll   r
        # "AAABABB"

        
        # max = 5
        # r
        # l
        #    while r-l-max <=k
        #     reduce cnt
        #     l+=1

        # llll rrrr
        # AAABABBBBCCCCCCA
        
        
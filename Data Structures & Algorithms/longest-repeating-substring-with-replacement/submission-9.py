class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        freq = {}
        maxF,l,res,r = 0,0,0,0
        while r<len(s):
            c = s[r]
            freq[c] = freq.get(c,0)+1
            maxF = max(maxF,freq[c])
            if r-l+1-maxF>k:
                freq[s[l]] -=1
                l+=1
            res = max(res,r-l+1)
            r+=1
        return res
            

            
            
            

        #                                 r
        # l           l
        # A   A   A   B   A   B   B   B   K   B


        # while r-l+1-maxF>k:
        #     reduce f
        #     l+=1

        
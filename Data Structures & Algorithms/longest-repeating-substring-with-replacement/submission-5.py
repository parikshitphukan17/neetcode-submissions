class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxF,res = 0,0
        cnt = defaultdict(int)
        l,r = 0,0
        N = len(s)
        while r<N:
            cnt[s[r]] +=1
            maxF = max(cnt[s[r]],maxF)
            while r-l+1 - maxF>k:
                cnt[s[l]] -=1
                l+=1
            res = max(res,r-l+1)
            r+=1
        return res


            
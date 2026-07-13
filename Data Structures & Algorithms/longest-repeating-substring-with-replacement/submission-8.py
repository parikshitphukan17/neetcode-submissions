class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
    # max 1   2   2   3   3   3.  4
    #     r   r   r   r   r   r   r
    #     l   l   l
    #     A   A   B   A   B   B   A

        l,r = 0,0
        maxF = 0
        cnt = defaultdict(int)
        res = 0
        while r<len(s):
            cnt[s[r]] +=1
            maxF = max(maxF,cnt[s[r]])
            while r-l+1-maxF>k:
                cnt[s[l]] -=1
                l+=1
            print(l,r,maxF)
            res = max(res,r-l+1)
            r+=1
        return res
            



    #     k = 2
    # maxF1   2   3   3   4   4   4   4   4   4   4   5
    #     r                   r   r   r   r   r   r   r
    #     l   l   l   l   l   l
    #     A   A   A   B   A   B   B   C   C   C   C   C

    #     while r-l+1-maxF>k:
    #         l++
        



        
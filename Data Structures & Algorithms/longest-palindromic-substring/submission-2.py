class Solution:
    def longestPalindrome(self, s: str) -> str:
        N = len(s)
        def getPalindrome(l,r):
            pal = ""
            while l>=0 and r<N and s[l] == s[r]:
                pal = s[l:r+1]
                l-=1
                r+=1
            return pal



        res = ""
        for i in range(N):
            res1 = getPalindrome(i,i)
            res2 = getPalindrome(i,i+1)
            tempRes = None
            if len(res1)>len(res2):
                tempRes = res1
            else:
                tempRes = res2
            if len(tempRes)>len(res):
                res = tempRes
        return res






        # ababd odd = l = i-1,r = i+1

        # abba even.  l = i-1 r= 1
         
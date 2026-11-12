class Solution:
    def longestPalindrome(self, s: str) -> str:
        N = len(s)
        def check(l,r):
            while l>=0 and r<N and s[l]==s[r]:
                l-=1
                r+=1
            return [l+1,r]
        resLen,res = 0,[]
        for i in range(len(s)):
            l,r = check(i,i)
            if r-l+1>resLen:
                resLen = r-l+1
                res = [l,r]
            l,r = check(i,i+1)
            if r-l+1>resLen:
                resLen = r-l+1
                res = [l,r]
        l,r = res
        return s[l:r]
            
            
        
        
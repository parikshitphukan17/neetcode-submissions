class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ["",0]
        for i in range(len(s)):
            #even
            l,r = i-1,i
            while l>=0 and r<len(s) and s[l] == s[r]:
                if r-l+1>res[1]:
                    res = [s[l:r+1],r-l+1]
                l,r = l-1,r+1
                
            
            #odd
            l,r = i,i
            while l>=0 and r<len(s) and s[l] == s[r]:
                if r-l+1>res[1]:
                    res = [s[l:r+1],r-l+1]
                l,r = l-1,r+1
                
        return res[0]

                
        
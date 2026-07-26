class Solution:
    def longestPalindrome(self, s: str) -> str:
        N = len(s)
        def palindrome(l,r):
            cur = [-1,-1,0]
            while l>=0 and r<N and s[l] == s[r]:
                cur = [l,r+1,r-l+1]
                l-=1
                r+=1
            return cur
        res = [-1,-1,0]
        for i in range(len(s)):
            cur1 = palindrome(i,i)
            cur2 = palindrome(i,i+1)
            if cur2[-1]>cur1[-1]:
                if cur2[-1]>res[-1]:
                    res = cur2
            else:
                if cur1[-1]>res[-1]:
                    res = cur1
        return s[res[0]:res[1]]

                
        

        



        
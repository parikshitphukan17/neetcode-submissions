class Solution:
    def longestPalindrome(self, s: str) -> str:
        N = len(s)
        def find(i1,i2):
            while i1>=0 and i2<N and s[i1] == s[i2]:
                i1-=1
                i2+=1
            return s[i1+1:i2]
        res = "" 
        for i in range(N):
            cur1,cur2 = find(i,i),find(i,i+1)
            res = max(res,cur1,cur2, key = len)
        return res

        




        # ababd
        # even = i,i+1
        # odd = i
        
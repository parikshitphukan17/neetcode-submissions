class Solution:
    def countSubstrings(self, s: str) -> int:
        N = len(s)
        cnt = 0
        def count(l,r):
            nonlocal cnt
            while l>=0 and r<N and s[l] == s[r]:
                cnt +=1
                l-=1
                r+=1
            return cnt
        
        for i in range(N):
            count(i,i)
            count(i,i+1)
        return cnt



        

            



        # a.     b      c
        # ab.      bc
        # abc
        
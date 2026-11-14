class Solution:
    def countSubstrings(self, s: str) -> int:
        cnt = 0
        N = len(s)
        def count(l,r):
            nonlocal cnt
            while l>=0 and r<N and s[l] == s[r]:
                cnt +=1
                l-=1
                r+=1
        
        for i in range(len(s)):
            count(i,i+1)
            count(i,i)
        return cnt



        
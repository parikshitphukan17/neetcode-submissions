class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        N = len(s)
        def count(l,r):
            count = 0
            while l>=0 and r<N and s[l] == s[r]:
                l-=1
                r+=1
                count +=1
            return count
        for i in range(N):
            res += count(i,i)
            res += count(i,i+1)
        return res





        
class Solution:
    def countSubstrings(self, s: str) -> int:
        N = len(s)
        def count(i1,i2):
            count = 0
            while i1>=0 and i2<N and s[i1]==s[i2]:
                count +=1
                i1 -=1
                i2 +=1
            return count
        res = 0
        for i in range(N):
            res += count(i,i)
            res += count(i,i+1)
        return res

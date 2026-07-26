class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        N = len(s)
        def cnt(l,r):
            nonlocal count
            while l>=0 and r<N and s[l] == s[r]:
                count +=1
                l-=1
                r+=1
        
        for i in range(len(s)):
            cnt(i,i)
            cnt(i,i+1)
        return count

                

    
        
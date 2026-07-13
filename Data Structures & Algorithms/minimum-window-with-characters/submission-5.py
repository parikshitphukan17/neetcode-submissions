class Solution:
    def minWindow(self, s: str, t: str) -> str:
        cnt1 = {} #s
        cnt2 = {} #t
        for i in t:
            cnt2[i] = cnt2.get(i,0)+1
        l= 0
        have,need = 0,len(cnt2)
        res,resLen = [-1,-1],float("infinity")
        for r in range(len(s)):
            cnt1[s[r]] = cnt1.get(s[r],0)+1
            if s[r] in cnt2 and cnt1[s[r]] == cnt2[s[r]]:
                have +=1
            while have == need:
                if resLen>r-l+1:
                    resLen,res= r-l+1,[l,r]
                cnt1[s[l]] -=1

                if s[l] in cnt2 and  cnt1[s[l]] +1 == cnt2[s[l]]:
                    have -=1
                l+=1
        l,r = res
        return s[l:r+1] if l!=-1 else ""
        
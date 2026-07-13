class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if s==t:
            return s
        cnt1,cnt2 = {},{}
        for c in t:
            cnt1[c] = cnt1.get(c,0)+1
        l=0
        have,need = 0,len(cnt1)
        res,resLen = [-1,-1],float('infinity')
        for r in range(len(s)):
            c=s[r]
            cnt2[s[r]] = cnt2.get(s[r],0)+1
            print(cnt1,cnt2,s[r])

            if c in cnt1 and cnt1[c] == cnt2[c]:
                have +=1
            print(have,need)
            while have == need:
                if resLen> r-l+1:
                    resLen = r-l+1
                    res = [l,r]
                cnt2[s[l]] -=1
                if s[l] in cnt1 and cnt2[s[l]]<cnt1[s[l]]:
                    have -=1
                l+=1
        
        l,r = res
        return s[l:r+1] if l!=-1 else ""
            




            
        
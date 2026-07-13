class Solution:
    def minWindow(self, s: str, t: str) -> str:
        cntT = Counter(t)
        need = len(cntT)
        l = 0
        have = 0
        cntS = defaultdict(int)
        res,resLen = [-1,-1],float("infinity")
        for r in range(len(s)):
            cntS[s[r]] += 1
            if s[r] in cntT:
                if cntT[s[r]] == cntS[s[r]]:
                    have +=1
            
            while have == need:
                if r-l+1<resLen:
                    res = [l,r]
                    resLen = r-l+1
                cntS[s[l]] -=1
                if s[l] in cntT and cntS[s[l]] +1 == cntT[s[l]]:
                    have -=1
                l+=1
        l,r = res
        return "" if -1 in res else s[l:r+1]


   

        
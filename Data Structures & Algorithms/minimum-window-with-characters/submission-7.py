class Solution:
    def minWindow(self, s: str, t: str) -> str:
        res =[-1,-1]
        tCnt = {}
        sCnt = {}
        for c in t:
            tCnt[c] =tCnt.get(c,0)+1
        have = 0
        need = len(tCnt)
        l,r,resLen = 0,0,float("inf")
        for r in range(len(s)):
            
            char = s[r]
            sCnt[char] =sCnt.get(char,0)+1
            if char in tCnt and sCnt[char] == tCnt[char]:
                have +=1
            while have == need:
                if r-l+1<resLen:
                    resLen = r-l+1
                    res = [l,r]
                sCnt[s[l]] -=1
                if s[l] in tCnt and tCnt[s[l]] > sCnt[s[l]]:
                    have -=1
                l +=1
        return s[res[0]:res[1]+1] if res[0]!=-1 else ""





        
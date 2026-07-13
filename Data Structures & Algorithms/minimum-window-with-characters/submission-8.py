class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l,r = 0,0
        res,resLen = [-1,-1],float("inf")
        cntW,cntT = {},{}
        for c in t:
            cntT[c] = cntT.get(c,0)+1
        need = len(cntT)
        have = 0
        N = len(s)
        while r<N:
            cntW[s[r]] = cntW.get(s[r],0)+1
            if s[r] in cntT and cntT[s[r]] == cntW[s[r]]:
                have +=1
            while have == need:
                if r-l+1<resLen:
                    res,resLen = [l,r],r-l+1
                cntW[s[l]] -=1
                if s[l] in cntT and cntW[s[l]] +1 == cntT[s[l]]:
                    have -=1
                l+=1
            r +=1
        return s[res[0]:res[1]+1] if res[0] != -1 else ""




        # 0   0   1   1   1   2   2   2   3
        # r   r   r   r   r   r   r   r   r   
        # l   l   l   l       
        # O   U   Z   O   D   Y   X   A   Z   V


        # X   Y   Z

        # need = 3
        # while have ==need:
        #     res = min(res,r-l+1)
        #     cntW[s[l]] -=1
        #     if s[l] in cntT and cntT[s[l]] == 1+ cntW[s[l]]:
        #         have -=1
            
        #     l+=1
        

            
        
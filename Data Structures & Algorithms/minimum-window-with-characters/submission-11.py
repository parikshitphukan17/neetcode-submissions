class Solution:
    def minWindow(self, s: str, t: str) -> str:
        ct,cs = {},{}
        matches = 0
        if len(t)>len(s):
            return ""
        for cur in t:
            if cur not in ct:
                ct[cur]= 0
                matches +=1
            ct[cur] +=1
        l,r,resLen,res,cur =0,0,float("inf"),[-1,-1],0

        while r<len(s):
            currentChar = s[r]
            cs[currentChar]= cs.get(currentChar,0)+1
            if currentChar in ct and ct[currentChar] == cs[currentChar]:
                cur+=1
            while cur==matches:
                leftChar = s[l]
                if r-l+1<resLen:
                    resLen = r-l+1
                    res = [l,r+1]
                cs[leftChar] -=1
                if leftChar in ct and cs[leftChar]<ct[leftChar]:
                    cur-=1
                l+=1
            r+=1
        return s[res[0]:res[1]] if res[0] !=-1 else ""



        # ct[
        #     x:1
        #     y:1
        #     z:1
        # ]
        # matches = 3
        # cur = 0
        # l       r
        # O   U   Z   O   D   Y   X   A   Z   V

        # if s[r] == t[r]:
        #     cur +=1
        
        # if cur == matches:
        #     res = r-l+1
        #     start contracting window
        #     cs[l] -=1
        #     if l in t:
        #         cur-=1
        
        
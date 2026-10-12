class Solution:

    def encode(self, strs: List[str]) -> str:
        val = ""
        for s in strs:
            val += str(len(s))+"#"+s
        print(val)
        return val
        

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i<len(s):
            l = i
            r= i
            while s[r]!= "#":
                r+=1
            length = int(s[l:r])
            l = r+1
            r= l+length
            res.append(s[l:r])
            i= r
        return res


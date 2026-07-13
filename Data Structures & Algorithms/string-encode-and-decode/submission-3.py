class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        for w in strs:
            s += str(len(w)) +"#" + w
        return s


    def decode(self, s: str) -> List[str]:
        i = 0
        res = []
        while i<len(s):
            j = i
            while s[j] != "#":
                j+=1
            cnt = int(s[i:j])
            start = j+1
            res.append(s[start:start+cnt])
            i = start+cnt
        return res
            

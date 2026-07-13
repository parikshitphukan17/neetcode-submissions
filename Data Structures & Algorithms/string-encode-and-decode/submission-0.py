class Solution:

    def encode(self, strs: List[str]) -> str:
        code = ""
        for s in strs:
            code += str(len(s))+"#" +s
        return code

        

    def decode(self, s: str) -> List[str]:
        i = 0
        res = []
        while i<len(s):
            j = i
            while s[j]!="#":
                j+=1
            l = int(s[i:j])
            j+=1 #actual word start
            res.append(s[j:j+l])
            i = j+l
        return res


                

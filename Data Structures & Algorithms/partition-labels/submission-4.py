class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = {}
        for i in range(len(s)):
            last[s[i]] = i

        i = 0
        l,r =0,0
        res = []
        while i<len(s):
            if i>r:
                res.append(r-l+1)
                l = i
            r = max(r,last[s[i]])
            i+=1
        res.append(r-l+1)
        return res
        
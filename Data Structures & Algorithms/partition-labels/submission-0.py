
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        res = []
        cnt = Counter(s)
        i = 0
        while i<len(s):
            subString = ""
            q = {}
            q[s[i]] = cnt[s[i]]
            while q:
                subString += s[i]
                cnt[s[i]] -=1
                if cnt[s[i]]:
                    q[s[i]] = cnt[s[i]]
                elif s[i] in q:
                    del q[s[i]]
                i+=1
            res.append(len(subString))
        return res


            
        
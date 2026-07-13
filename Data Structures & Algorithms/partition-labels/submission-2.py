class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        cnt = Counter(s)
        i,l = 0,len(s)
        res =[]
        while i<l:
            j = i
            cntSeg = {}
            cntSeg[s[j]] = cnt[s[j]]
            while len(cntSeg)>0 and j<l:
                cnt[s[j]] -=1
                if not cnt[s[j]]:
                    cnt.pop(s[j])
                    if s[j] in cntSeg:
                        cntSeg.pop(s[j])
                else:
                    cntSeg[s[j]] = cnt[s[j]]
                j+=1
            res.append(j-i)
            i =j
        return res
            
                


        
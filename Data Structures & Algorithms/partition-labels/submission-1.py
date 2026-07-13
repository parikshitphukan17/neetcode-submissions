class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        cnt = defaultdict(int)
        for char in s:
            cnt[char] +=1
        i = 0
        res = []
        while i<len(s):
            word = ""
            wordCnt = {}
            wordCnt[s[i]] = cnt[s[i]]
            while wordCnt:
                word += s[i]
                cnt[s[i]] -=1
                if cnt[s[i]]:
                    wordCnt[s[i]] = cnt[s[i]]
                elif s[i] in wordCnt:
                    wordCnt.pop(s[i])
                i+=1
            res.append(len(word))
        return res




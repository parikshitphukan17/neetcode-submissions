class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        s1Cnt,s2Cnt = [0]*26, [0]*26
        for i in range(len(s1)):
            s1Cnt[ord(s1[i])-ord('a')]+=1
            s2Cnt[ord(s2[i])-ord('a')]+=1
        matches = 0
        for i in range(26):
            matches += (1 if s1Cnt[i]== s2Cnt[i] else 0)
        if matches == 26:
            return True
        l = 0
        for r in range(len(s1),len(s2)):
            li = ord(s2[l]) - ord('a')
            s2Cnt[li] -=1
            if s2Cnt[li] + 1 == s1Cnt[li]:
                matches -= 1
            elif s2Cnt[li] == s1Cnt[li]:
                matches += 1
            l+=1
            ri = ord(s2[r]) - ord('a')
            s2Cnt[ri] +=1
            if s2Cnt[ri] == s1Cnt[ri]:
                matches += 1
            elif s2Cnt[ri] -1 == s1Cnt[ri]:
                matches -=1
            if matches == 26:
                return True
        return False









        # a   b   c.     [00000...111]
        # l   e   c.     [00.1..e.c0000]

        # matches = 12

        # for r in range(3,len):
        #     s2[l] -=1
        #     if s2[l]+1 == s1[l]:
        #         matches -=1
        #     elif s2[l] == s1[l]:
        #         matches +=1
        #     s2[r] +=1
        #     if s2[r] == s1[r]:
        #         matches +=1
        #     elif s2[r]. -1 == s1[r]:
        #         matches -=1
        #     i fmatches == 26:
        #     return True





        
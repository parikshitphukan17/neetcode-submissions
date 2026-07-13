class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        s1Cnt,s2Cnt = [0]*26,[0]*26
        for i in range(len(s1)):
            s1Cnt[ord(s1[i])- ord('a')]+=1
            s2Cnt[ord(s2[i])- ord('a')]+=1
        matches = 0
        for i in range(26):
            matches += (1 if s1Cnt[i] == s2Cnt[i] else 0)
        l = 0
        for r in range(len(s1),len(s2)):
            if matches == 26:
                return True
            s2Cnt[ord(s2[r])-ord('a')] +=1
            if s2Cnt[ord(s2[r])-ord('a')] == s1Cnt[ord(s2[r])-ord('a')]:
                matches +=1
            elif s2Cnt[ord(s2[r])-ord('a')] -1 == s1Cnt[ord(s2[r])-ord('a')]:
                matches -=1
            s2Cnt[ord(s2[l])-ord('a')] -=1
            if s2Cnt[ord(s2[l])-ord('a')] == s1Cnt[ord(s2[l])-ord('a')]:
                matches +=1
            elif s2Cnt[ord(s2[l])-ord('a')] +1 == s1Cnt[ord(s2[l])-ord('a')]:
                matches -=1
            l+=1
        return matches == 26
            
   
            


            
        
            

        

        




        
        
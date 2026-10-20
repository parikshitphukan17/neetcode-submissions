class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2)<len(s1):
            return False

        matches = 0
        c1,c2 = [0]*26,[0]*26
        for i in range(len(s1)):
            c1[ord(s1[i])-ord("a")]+=1
            c2[ord(s2[i])-ord("a")]+=1
        for i in range(26):
            matches += (1 if c1[i] == c2[i] else 0)
        if matches == 26:
            return True
        l,r = 0, len(s1)
    
        while r<len(s2):
            ordVal = ord(s2[l])-ord("a")
            l+=1
            c2[ordVal] -=1
            if c2[ordVal] == c1[ordVal]:
                matches +=1
            elif c2[ordVal] +1 ==  c1[ordVal]:
                matches -=1
            ordVal = ord(s2[r])-ord("a")
            c2[ordVal] +=1
            if c2[ordVal] == c1[ordVal]:
                matches +=1
            elif c2[ordVal] -1 == c1[ordVal]:
                matches -=1
            if matches == 26:
                return True
            r+=1
            
        return False



            
            
        



        # l   e   c   a   a   b   e   e



        # a   b   c

        # [0  0   0   ..  1   1   1]




        # a   b   c == l  e   c
        # matches = 26:
        #     return True
        
        # remove l 
        # if c2[l] == c1[l]:
        #     match +1
        # elif c2[l] +1 ==c1[l]:
        #     match +1
        
        # r +1
        # if c2[r] == c1[r]:
        #     match +1
        # if c2[r]-1 == c1[r]:
        #     match -1

        
        
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        cnt = Counter(hand)
        i = min(hand)
        while i<=max(hand):
            if i not in cnt or cnt[i] == 0:
                i+=1
                continue
            l = i
            for j in range(l,l+groupSize):
                print(j,cnt)
                if j not in cnt or cnt[j] == 0:
                    return False
                cnt[j] -=1
        return True

        
                


        
        
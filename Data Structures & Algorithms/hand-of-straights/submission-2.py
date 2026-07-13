class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:

        cnt = Counter(hand)
        
        
        for i in sorted(hand):
            if i in cnt:
                for j in range(i,i+groupSize):
                    if j not in cnt:
                        return False
                    if cnt[j] == 1:
                        cnt.pop(j)
                    else:
                        cnt[j] -=1
        return True

        # {1-2
        # 2-2
        # 3-2}


        
        
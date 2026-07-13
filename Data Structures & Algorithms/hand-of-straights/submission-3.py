class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        hand.sort()
        cnt = Counter(hand)
        i = hand[0]

        while i<=hand[-1]:
            if i not in cnt:
                i+=1
                continue
            j = i
            for j in range(j,j+groupSize):
                if j not in cnt:
                    return False
                cnt[j] -= 1
                if cnt[j] == 0:
                    cnt.pop(j)
            if i not in cnt:
                i+=1
        return True
            
                

        
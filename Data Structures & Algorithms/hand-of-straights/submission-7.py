class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        cnt = Counter(hand)
        for i in range(min(hand),max(hand)+1,1):
            if i not in cnt or cnt[i] == 0:
                continue
            while cnt[i]>0:
                for j in range(i,i+groupSize,1):
                    if j not in cnt or not cnt[j]:
                        return False
                    cnt[j] -=1
        return True
        
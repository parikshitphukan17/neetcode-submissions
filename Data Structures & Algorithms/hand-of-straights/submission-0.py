class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand)%groupSize:
            return False
        cnt = defaultdict(int)
        for i in hand:
            cnt[i] +=1
        for num in sorted(hand):
            if cnt[num]:
                for i in range(num,num+groupSize):
                    if cnt[i] == 0:
                        return False
                    cnt[i] -=1
        return True
        
        

        
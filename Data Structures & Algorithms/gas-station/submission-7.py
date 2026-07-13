class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        g,c = 0,0
        for i in range(len(gas)):
            g+=gas[i]
            c+=cost[i]
            gas[i] = gas[i] - cost[i]
        if g<c:
            return -1
        ans = -1
        cur = 0
        for i in range(len(gas)):
            cur = cur+gas[i]
            if cur>=0:
                if  ans == -1:
                    ans = i
            else:
                cur = 0
                ans = -1
        return ans

        # -2 -2 -2 3 3
        
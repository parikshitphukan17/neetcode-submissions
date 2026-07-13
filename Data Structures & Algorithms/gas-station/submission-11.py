class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(cost)>sum(gas):
            return -1
        cur = 0
        res = None
        for i in range(len(gas)):
            curCost =  gas[i]-cost[i]
            if curCost>=0 and not res:
                res =i
                cur = 0
            cur += curCost
            if res and cur<0:
                res = None

        return res if res is not None else -1




    #   2,-1,-1


        # -1,-1,1,2

        # -1,-2,-1,1


        -2,-2,-2,3,3

        
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas)<sum(cost):
            return -1
        res = 0
        diff = 0
        for i in range(len(gas)):
            diff += gas[i]-cost[i]
            if diff<0:
                res = i+1
                diff = 0
        return res



        # 1  2  3  4
        # 2  2  4  1
        # -1 0  -1. 3 
        
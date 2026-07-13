import math

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pos =[]
        for i in range(len(position)):
            pos.append([position[i],speed[i]])
        pos.sort()

        last = -float("infinity")
        res = 0
        for i in range(len(pos)-1,-1,-1):
            p,s = pos[i]
            reachTime = float(target-p)/s
            if last ==   -float("infinity"):
                last = reachTime
                continue
            if last<reachTime: #create new fleet
                res +=1
                last = reachTime
        return res+1
                


        
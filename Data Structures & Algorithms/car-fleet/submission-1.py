import math

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pos =[]
        for i in range(len(position)):
            pos.append([position[i],speed[i]])
        pos.sort()

        stack = []
        res = 0
        for i in range(len(pos)-1,-1,-1):
            p,s = pos[i]
            reachTime = float(target-p)/s
            if not stack:
                stack.append(reachTime)
                continue
            if stack[-1]>= reachTime: #make fleet
                stack.append(stack[-1])
            else:
                res +=1
                stack = [reachTime]
        return res+1
                


        
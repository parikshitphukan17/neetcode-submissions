class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pos =[]
        stack = []
        for i in range(len(position)):
            pos.append([position[i],speed[i]])
        pos.sort()
        for i in range(len(pos)-1,-1,-1):
            req = (target-pos[i][0])/pos[i][1]
            if stack and stack[-1]>=req:
                continue
            stack.append(req)
        return len(stack)

        
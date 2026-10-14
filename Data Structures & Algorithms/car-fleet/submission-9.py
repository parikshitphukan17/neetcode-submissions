class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        ps = []
        for i in range(len(position)):
            ps.append([position[i],speed[i]])
        ps.sort(key = lambda x: (-x[0]))
        fleet = []
        for pos,sp in ps:
            t = (target-pos)/sp
            if not fleet or fleet[-1]<t:
                fleet.append(t)
        return len(fleet)




        # [3,5,10,3]


        # [[4,2], [1,2], [0,1], [7,1]]

        # [[7,1], [4,2], [1,2], [0,1]]


        # [3,5,]


        # [6  3   5]
        
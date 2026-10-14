class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        for i,t in enumerate(temperatures):
            while stack and stack[-1][1]<t:
                prevI,prevT = stack.pop()
                temperatures[prevI] = i-prevI
            stack.append([i,t])
        while stack:
            prevI,prevT = stack.pop()
            temperatures[prevI] = 0
        return temperatures






                                
        # 30  38  30  36  35  40  28
        
        # [30]

        # [38]
        # 1  38  30  36  35  40  28

        # [38,30]
        # 1  38  30  36  35  40  28

        # [38,36]
        # 1  38  1  36  35  40  28

        # [38,36,35]
        # 1  38  1  36  35  40  28

        # [40]
        # 1  4  1  2  1  40  28

        # for each value pop till smaller and fill value then insert

        # post loop if stack not empty fill value with 0




        


       
        # pop till empty or found greater value




        
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0]*(len(temperatures))
        for i in range(len(temperatures)-1,-1,-1):
            t = temperatures[i]
            while stack and stack[-1][0]<=t:
                stack.pop()
            if stack:
                res[i] = stack[-1][1] - i
            stack.append([t,i])
        return res
                



    
    


        #check if last value greater?
        #if not pop till greater or empty
            #if empty put 0
        #else:
        #put val and insert cur val to stack



        
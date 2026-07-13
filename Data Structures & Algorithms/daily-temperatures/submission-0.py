class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)
        for i in range(len(temperatures)):
            if not stack:
                stack.append([temperatures[i],i])
                continue
            while stack and stack[-1][0]<temperatures[i]:
                prevVal,prev = stack.pop()
                res[prev] = i-prev
            stack.append([temperatures[i],i])
        return res



        
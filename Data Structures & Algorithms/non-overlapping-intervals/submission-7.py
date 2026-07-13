class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        prevY = -50001
        res = 0
        for i,j in intervals:
            if i>= prevY:
                prevY = j
            else:
                res +=1
                prevY = min(prevY,j)
        return res        
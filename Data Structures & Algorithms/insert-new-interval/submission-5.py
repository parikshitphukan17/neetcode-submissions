class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        for i in range(len(intervals)):
            cur = intervals[i]
            if newInterval[0]<cur[0]:
                cur = newInterval
                newInterval = intervals[i]
            curx,cury = cur
            newx,newy = newInterval

            if newx>cury:
                res.append(cur)
            elif newx<=cury and newx>= curx:
                newInterval = [min(curx,newx),max(cury,newy)]
            else:
                res.append(newInterval)
                return res + intervals[i:]
        res.append(newInterval)
        return res




        
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        for i in range(len(intervals)):
            newStart,newEnd = newInterval
            start,end = intervals[i]
            if end<newStart:
                res.append(intervals[i])
            elif newEnd<start:
                res.append(newInterval)
                res = res + intervals[i:]
                return res
            elif newStart<=newEnd:
                newInterval = [min(newStart,start),max(end,newEnd)]
        res.append(newInterval)
        return res

        
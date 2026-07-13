class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        for i in range(len(intervals)):
            start,end = intervals[i]
            newStart,newEnd = newInterval
            if newEnd<start:
                res.append(newInterval)
                return res + intervals[i:]
            elif newStart<=end:
                newInterval = [min(newStart,start),max(end,newEnd)]
            else:
                res.append([start,end])
        res.append(newInterval)
        return res
            






        # if newStart before end

        # if newstart after end:
        #     res .append(old)
        # if newend before start:
        #     enter extra + rest
        
        
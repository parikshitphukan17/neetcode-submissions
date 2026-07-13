class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = []
        res.append(intervals[0])
        last = intervals[0][1]
        for start,end in intervals[1:]:
            if start<=last:
                prevStart,prevEnd = res.pop()
                res.append([min(prevStart,start),max(prevEnd,end)])
            else:
                res.append([start,end])
            last = res[-1][1]
        return res


        
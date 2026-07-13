class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])
        res = []
        for start,end in intervals:
            if not res:
                res.append([start,end])
                continue
            last = res[-1][1]
            if last>=start:
                lastStart,lastEnd = res.pop()
                res.append([min(start,lastStart),max(end,lastEnd)])
            else:
                res.append([start,end])
        return res
        
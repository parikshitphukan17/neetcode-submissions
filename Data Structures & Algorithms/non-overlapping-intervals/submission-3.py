class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[0])
        last = intervals[0]
        res = 0
        for start,end in intervals[1:]:
            prevStart,prevEnd = last
            if start<prevEnd:
                res +=1
                last = [max(prevStart,start),min(end,prevEnd)]
            else:
                last = [start,end]
        return res

        
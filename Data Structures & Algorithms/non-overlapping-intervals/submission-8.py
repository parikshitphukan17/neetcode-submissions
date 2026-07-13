class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x:x[0])
        last = None
        res = 0
        for start,end in intervals:
            if not last:
                last = end
                continue
            if last>start:
                res +=1
                last = min(last,end)
            else:
                last = end
        return res
            
        
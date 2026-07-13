class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort()
        res = [intervals[0]]
        for start,end in intervals[1:]:
            prevStart,prevEnd = res[-1]
            if start<= prevEnd:
                res.pop()
                res.append([min(prevStart,start),max(prevEnd,end)])
            else:
                res.append([start,end])
        return res

        
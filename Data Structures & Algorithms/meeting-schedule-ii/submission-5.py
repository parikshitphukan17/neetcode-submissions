"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        res =0
        heap = []
        intervals.sort(key=lambda x:x.start)
        for i in range(len(intervals)):
            start,end = intervals[i].start,intervals[i].end
            while heap and heap[0]<=start:
                heapq.heappop(heap)
            heapq.heappush(heap,end)
            res = max(res,len(heap))
        return res

        
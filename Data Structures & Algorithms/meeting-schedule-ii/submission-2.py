"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:

        intervals.sort(key=lambda x:x.start)
        start,end = [],[]
        for i in intervals:
            start.append(i.start)
            end.append(i.end)
        end.sort()

        i,j = 0,0
        day = 0
        res = 0
        while i <len(start) and j<len(end):
            if end[j]<=start[i]:
                day -=1
                j+=1
            else:
                day +=1
                i+=1
            res = max(day,res)
        return res
            

        
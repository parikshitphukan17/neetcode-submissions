"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start,end = [],[]
        for i in intervals:
            start.append(i.start)
            end.append(i.end)
        start.sort()
        end.sort()
        res = 0
        rooms = 0
        i = 0
        j = 0
        while i<len(start):
            if start[i]<end[j]:
                rooms +=1
                res = max(rooms,res)
                i+=1
            else:
                rooms -=1
                j+=1
        return res



        
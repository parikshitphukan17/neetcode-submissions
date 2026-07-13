class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        for i in range(len(intervals)):
            start,end = intervals[i]
            newStart,newEnd = newInterval
            if newStart>end:
                res.append([start,end])
            elif newEnd<start:
                res.append(newInterval)
                return res + intervals[i:]
            else:
                newInterval = [min(start,newStart),max(end,newEnd)]
        res.append(newInterval)
        return res



    #     [[1,2].[3,5],[9,10]]
        

    #     [1,2], [3,5], [6,7],[9,10]


    # [[4,6]].  [1,5]
    # 1>6
    # if newInterval[0]>interval[i][1]
    #     insert interval
    # 5<4
    # if newInterVal[1]<intervals[i][0]:
    #     insert newInterval then rest
    # else:
    #     newInterval = merge with current interval


    
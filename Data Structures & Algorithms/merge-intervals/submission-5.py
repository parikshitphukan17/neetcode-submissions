class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        prevX,prevY = -1,-1
        res = []
        for i,j in intervals:
            if i>prevY:
                res.append([i,j])
                prevX = i
                prevY = j
            else:
                res.pop()
                prevX,prevY = min(i,prevX), max(j,prevY)
                res.append([prevX,prevY])
        return res


        
class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        res = {}
        i = 0
        intervals.sort(key = lambda x:x[0])
        heap = []
        for q in sorted(queries):
            while i<len(intervals) and q>= intervals[i][0]:
                if q<= intervals[i][1]:
                    heapq.heappush(heap,[intervals[i][1]-intervals[i][0]+1,intervals[i][1]])
                i+=1
            while heap and heap[0][1]<q:
                heapq.heappop(heap)
            if heap:
                res[q] = heap[0][0]
            else:
                res[q] = -1
        return [res[q] for q in queries]




        
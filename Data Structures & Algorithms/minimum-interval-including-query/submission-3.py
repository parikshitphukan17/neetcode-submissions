import heapq

class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        minIntervals = {}
        heap = []
        intervals.sort()
        i = 0
        for q in sorted(queries):
            while heap and heap[0][1]<q:
                heapq.heappop(heap)
            while i<len(intervals) and q>=intervals[i][0] :
                if q<=intervals[i][1]:
                    heapq.heappush(heap,[intervals[i][1]-intervals[i][0]+1,intervals[i][1]])
                i+=1
            minIntervals[q] = heap[0][0] if heap else -1
        return [minIntervals[q] for q in queries]
        
            


        
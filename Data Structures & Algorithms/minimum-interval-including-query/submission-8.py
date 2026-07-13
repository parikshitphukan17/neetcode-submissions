class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:

        intervals.sort()
        j = 0
        heap = []
        resM = {}
        for i in sorted(queries):
            while j<len(intervals) and intervals[j][0] <=i:
                heapq.heappush(heap,[intervals[j][1]-intervals[j][0]+1,intervals[j][1]])
                j+=1
            while heap and heap[0][1]<i:
                heapq.heappop(heap)
            resM[i] = heap[0][0] if heap else -1
        res = [resM[i] for i in queries]
        return res
            



        
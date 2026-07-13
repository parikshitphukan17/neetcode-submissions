class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        i = 0
        N = len(intervals)
        intervals.sort()
        res = {}
        heap = []
        for q in sorted(queries):
            while i<N and intervals[i][0]<=q:
                start,end = intervals[i]
                heapq.heappush(heap,[end-start+1,end])
                i+=1
            while heap and heap[0][1]<q:
                heapq.heappop(heap)
            
            res[q] = heap[0][0] if heap else -1
        return [res[q] for q in queries]




        
        # [1,2,3,6,7,8].   [[3,3]].     {1:3}
        # [3,6,7,8].   [[3,3],[2,3]].   {1:3,2:2}
        # pop till valid
        # insert till possible
        # get 0th u¥in heap or -1


        
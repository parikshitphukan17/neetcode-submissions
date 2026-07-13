class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for i, (x, y) in enumerate(points):
            heapq.heappush(heap,[x*x + y*y,i])
        res = []
        while k>0:
            d,i = heapq.heappop(heap)
            res.append(points[i])
            k-=1
        return res

        
        
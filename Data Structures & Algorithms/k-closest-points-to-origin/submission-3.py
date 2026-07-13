class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        res = []
        for x,y in points:
            heapq.heappush(heap,[x**2+y**2,x,y])
        while k>0:
            d,x,y = heapq.heappop(heap)
            res.append([x,y])
            k-=1
        return res
        
import heapq
import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        res = []
        for x,y in points:
            heapq.heappush(heap,[math.sqrt((x*x)+ (y*y)),x,y])
        print(heap)
        while k>0:
            val,x,y = heapq.heappop(heap)
            res.append([x,y])
            k-=1
        return res
            

        
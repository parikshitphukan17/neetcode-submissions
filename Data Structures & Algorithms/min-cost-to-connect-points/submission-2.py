import heapq

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        heap =[]
        res = 0
        adj = defaultdict(list)
        for i in range(len(points)):
            x,y = points[i]
            for j in range(1,len(points)):
                nx,ny = points[j]
                dist = abs(x-nx) + abs(y-ny)
                adj[i].append([dist,j])
                adj[j].append([dist,i])
        heap = [[0,0]]
        vis = set()
        while heap and len(vis)<len(points):
            d,src = heapq.heappop(heap)
            if src in vis:
                continue
            vis.add(src)
            res+=d
            for dist,dest in adj[src]:
                heapq.heappush(heap,[dist,dest])
        return res
            


        
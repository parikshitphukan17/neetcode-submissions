import heapq

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def dist(x1,x2,y1,y2):
            return abs(x1-x2) + abs(y1-y2)
        
        adj = defaultdict(list)

        for i in range(len(points)):
            x1,y1 = points[i]
            for j in range(i+1,len(points)):
                x2,y2 = points[j]
                cost=dist(x1,x2,y1,y2)
                adj[i].append([cost,j])
                adj[j].append([cost,i])
        vis = set()
        heap = [[0,1]]
        res = 0
        while heap:
            c,s = heapq.heappop(heap)
            if s in vis:
                continue
            vis.add(s)
            res += c
            for c2,d in adj[s]:
                heapq.heappush(heap,[c2,d])
        return res




        
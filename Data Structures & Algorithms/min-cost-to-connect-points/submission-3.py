import heapq

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        heap =[[0,0]]
        res = 0
        adj = defaultdict(list)
        for i in range(len(points)):
            x,y = points[i]
            for j in range(1,len(points)):
                nx,ny = points[j]
                dist = abs(x-nx) + abs(y-ny)
                adj[i].append([dist,j])
                adj[j].append([dist,i])
        
        vis = set()
        res = 0
        while heap:
            l,s = heapq.heappop(heap)
            if s in vis:
                continue
            res +=l
            vis.add(s)
            for d,np in adj[s]:
                heapq.heappush(heap,[d,np])
        return res

            
        

        
            


        
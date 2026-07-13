import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        heap = []
        adj =defaultdict(list)
        for u,v,t in times:
            adj[u].append([t,v])
        
        heapq.heappush(heap,[0,k])
        vis = set()
        res = 0
        while heap:
            t,u = heapq.heappop(heap)
            if u in vis:
                continue
            res = max(res,t)
            vis.add(u)
            for t2,v in adj[u]:
                heapq.heappush(heap,[t+t2,v])
        return res if len(vis) ==n else -1
        
        
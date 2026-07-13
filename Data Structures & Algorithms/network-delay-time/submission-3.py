import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        for src,d,t in times:
            adj[src].append([t,d])
        heap = [[0,k]]
        vis = set()
        res = 0
        while heap:
            cur,s = heapq.heappop(heap)
            if s in vis:
                continue
            vis.add(s)
            res = max(res,cur)
            for t,d in adj[s]:
                heapq.heappush(heap,[t+cur,d])
        return res if len(vis) ==n else -1


    
        
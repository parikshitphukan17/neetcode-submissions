import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        for s,d,c in times:
            adj[s].append([c,d])
        heap = []
        vis = set()
        heapq.heappush(heap,[0,k])
        res = 0
        while heap:
            while heap:
                c,s = heapq.heappop(heap)
                if s in vis:
                    continue
                res = max(res,c)
                vis.add(s)
                for c2,d in adj[s]:
                    heapq.heappush(heap,[c+c2,d])
        return -1 if len(vis)<n else res


        
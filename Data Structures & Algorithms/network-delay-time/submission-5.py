import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)

        for src,d,t in times:
            adj[src].append([t,d])
        
        vis = set()
        res = 0
        heap = [[0,k]]
        while heap and len(vis)<n:
            t,s =heapq.heappop(heap)
            if s in vis:
                continue
            vis.add(s)
            res = t
            for t,nei in adj[s]:
                heapq.heappush(heap,[res+t,nei])
        return res if len(vis) == n else -1

        
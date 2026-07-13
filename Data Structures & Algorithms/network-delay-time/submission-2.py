class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        heap = [[0,k]]
        adj = defaultdict(list)
        for src,des,time in times:
            adj[src].append([time,des])
        
        vis = set()
        res = 0
        while heap:
            child = []
            while heap:
                time,src = heapq.heappop(heap)
                if src in vis:
                    continue
                vis.add(src)
                res = max(res,time)
                for t,des in adj[src]:
                    heapq.heappush(heap,[time+t,des])
        return res if len(vis) == n else -1

        
        

        
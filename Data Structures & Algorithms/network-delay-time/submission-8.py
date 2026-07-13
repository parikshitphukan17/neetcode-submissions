class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        res = 0
        adj = {i:[] for i in range(1,n+1,1)}
        for src,dest,c in times:
            adj[src].append([c,dest])
        heap = [[0,k]]
        vis = set()
        while heap and len(vis)<=n:
            c,src = heapq.heappop(heap)
            if src in vis:
                continue
            vis.add(src)
            res = c
            for cost,dest in adj[src]:
                heapq.heappush(heap,[cost+c,dest])
        return res if len(vis) == n else -1



        
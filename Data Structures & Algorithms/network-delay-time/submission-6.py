class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        res = 0
        adj = {i:[] for i in range(n+1)}
        for src,dest,cost in times:
            adj[src].append([cost,dest])
        heap = [[0,k]]
        vis = set()
        while heap and len(vis)<n:
            cost,src = heapq.heappop(heap)
            if src in vis:
                continue
            vis.add(src)
            res = max(res,cost)
            for nextCost,dest in adj[src]:
                heapq.heappush(heap,[nextCost+cost,dest])
        return res if len(vis)==n else -1
        
            

        
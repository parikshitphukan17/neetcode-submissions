class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = {i:[] for i in range(1,n+1,1)}
        for i,j,c in times:
            adj[i].append([c,j])
        heap = []
        heapq.heappush(heap,[0,k])
        vis = set()
        res = 0
        while heap and len(vis)<n:
            c,node = heapq.heappop(heap)
            if node in vis:
                continue
            vis.add(node)
            res = c
            for cost,j in adj[node]:
                heapq.heappush(heap,[c+cost,j])
        return res if len(vis) == n else -1
            

            
        
        
        
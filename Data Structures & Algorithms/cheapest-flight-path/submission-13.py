class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = {i:[] for i in range(n)}
        for s,d,cost in flights:
            adj[s].append([d,cost])
        res = 1001
        heap = [[0,src]]
        k+=1
        vis = {}
        while k>=0:
            nextHeap = []
            while heap:
                cost,air = heapq.heappop(heap)
                if air == dst:
                    res = min(res,cost)
                if air in vis and vis[air]<cost:
                    continue
                vis[air] = cost
                for d,c in adj[air]:
                    heapq.heappush(nextHeap, [cost+c,d])
            heap = nextHeap
            k-=1
        return -1 if res == 1001 else res



                
        
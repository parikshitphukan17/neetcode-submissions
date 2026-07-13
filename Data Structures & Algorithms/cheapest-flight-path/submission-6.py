class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        k+=1
        heap = [[0,src]]
        res = float("inf")
        adj = defaultdict(list)
        for s,d,p in flights:
            adj[s].append([p,d])
        while k+1 and heap:
            nextHeap = []
            while heap:
                p,s = heapq.heappop(heap)
                if s == dst:
                    res = min(res,p)
                for np,d in adj[s]:
                    heapq.heappush(nextHeap,[p+np,d])
            heap = nextHeap
            k-=1
        return res if res != float("inf") else -1

                
        
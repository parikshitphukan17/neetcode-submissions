import heapq

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = defaultdict(list)
        res = float("infinity")
        for s,dest,price in flights:
            adj[s].append([price,dest])
        heap = []
        print(adj)
        for dest,price in adj[src]:
            heapq.heappush(heap,[dest,price])
        while k>=0:
            print(heap)
            k-=1
            nextHeap = []
            while heap:
                price,s = heapq.heappop(heap)
                if s == dst:
                    res = min(res,price)
                    continue
                for p,dest in adj[s]:
                    heapq.heappush(nextHeap,[p+price,dest])
            heap = nextHeap
        return res if res!= float("infinity") else -1

        
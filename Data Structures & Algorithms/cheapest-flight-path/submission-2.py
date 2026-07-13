import heapq

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        res = float("infinity")
        heap = [[0,src]]
        adj = defaultdict(list)
        for s,d,p in flights:
            adj[s].append([p,d])
        
        while heap and k+1>=0:
            heap2 = []
            while heap:
                p,s = heapq.heappop(heap)
                if s == dst:
                    res = min(res,p)
                for p2,d in adj[s]:
                    heapq.heappush(heap2,[p+p2,d])
            heap =heap2
            k-=1
        return res if res!= float("infinity") else -1 
        
        

        
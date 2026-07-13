class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        res = 1001
        k +=1
        vis = set()
        adj = {i:[] for i in range(n)}
        for s,d,p in flights:
            adj[s].append([p,d])
        heap = [[0,src]]
        while k>=0:
            nextHeap = []
            while heap:
                c,cur = heapq.heappop(heap)
                if cur == dst:
                    res = min(res,c)
                if cur in vis:
                    continue
                vis.add(cur)
                for p,d in adj[cur]:
                    heapq.heappush(nextHeap,[p+c,d])
            k-=1
            heap = nextHeap
        return res if res<1001 else -1



        # k = 2
        # heap = [[0,src]]

        # k = 1
        # [200,1]


        # k= 0
        # [500,3]




        
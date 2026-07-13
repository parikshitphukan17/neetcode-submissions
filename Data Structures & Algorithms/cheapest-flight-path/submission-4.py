import heapq

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        res = float("infinity")
        k+=1
        heap = [[0,src]]
        adj = defaultdict(list)
        for s,des,c in flights:
            adj[s].append([c,des])

        vis = set()
        while heap and  k>=0:
            next = []
            while heap:
                c,s = heapq.heappop(heap)
                if s == dst:
                    res = min(res,c)
                if s in vis:
                    continue
                vis.add(s)
                for neiC,nei in adj[s]:
                    heapq.heappush(next,[c+neiC,nei])
            k-=1
            heap = next
        return -1 if res == float("infinity") else res





  
        # [0,0]      2


        # [200,1].    1

        # [500,3].   0



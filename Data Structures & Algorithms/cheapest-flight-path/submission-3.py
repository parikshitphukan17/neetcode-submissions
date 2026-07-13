class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        k +=1
        adj = defaultdict(list)
        for s,des,p in flights:
            adj[s].append([p,des])

        res = float("infinity")
        heap = [[0,src]]
        while heap and k>=0:
            child = []
            while heap:
                p,s = heapq.heappop(heap)
                if s == dst:
                    res = min(res,p)
                for np,nei in adj[s]:
                    heapq.heappush(child,[np+p,nei])
            heap = child
            k -=1
        return -1 if res == float("infinity") else res
        
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        heap = [[0,k]]
        adj = {i:[] for i in range(1,n+1,1)}
        for s,d,t in times:
            adj[s].append([t,d])
        vis = set()
        res = 0
        while heap and len(vis) <n:
            t,s = heapq.heappop(heap)
            if s in vis:
                continue
            vis.add(s)
            res = max(res,t)
            for time,d in adj[s]:
                heapq.heappush(heap,[t+time,d])
        return res if len(vis) ==n else -1

        


        

        
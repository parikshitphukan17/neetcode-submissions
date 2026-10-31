class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        heap = []
        cnt = Counter(tasks)
        for k in cnt:
            heapq.heappush(heap,[-cnt[k],k])
        q = deque([])
        t = 0
        n+=1
        while heap or q:
            if not heap or (q and q[0][0]<=t):
                qt,qcnt = q.popleft()
                t = max(t,qt)
                heapq.heappush(heap,qcnt)
            maxCnt,task = heapq.heappop(heap)
            maxCnt +=1
            if maxCnt<0:
                q.append([t+n,[maxCnt,task]])
            t+=1
        return t
        
            
    #     t = 1



    # q []               2X2Y
    #             2X
    #             x-1
    # [3,X ]            2Y
    #     t = 2

    #             2Y
    #             Y-1
    # [4,X 5,Y].       

    # t = 3
    # empty or q<cur
    # t = max(cur,qpop)
    # insert into hea@
    


        
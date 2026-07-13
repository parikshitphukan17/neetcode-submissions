import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        heap = []
        cnt = Counter(tasks)
        for k in cnt:
            heapq.heappush(heap,[-cnt[k],k])
        q = deque()
        n+=1
        t = 1
        while q or heap:
            print(q,heap,t)
            if not heap:
                t = max(q[0][0],t)
            while q and q[0][0]<=t:
                time,c,task = q.popleft()
                heapq.heappush(heap,[c,task])
            c,task = heapq.heappop(heap)
            if c+1:
                q.append([t+n,c+1,task])
            t +=1
        return t-1
            
        

        # t = 1
        # 3A,B,C.    q [[4,2,A]]
        # t =2
        # B,C q[[4,2,A]]
        # t=3
        # C q[[4,2,A]]
        # t = 4.   
        # q[[4,2,A]]
        # if no heap t = q[0][0]
        # start poping and insert to heap t == q[0][0] or no heap:
        # if no heap:
        #     t = q[0]
        # 2A



        
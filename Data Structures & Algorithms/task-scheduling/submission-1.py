import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        cnt = Counter(tasks)
        heap =[[-cnt,task] for task,cnt in cnt.items()]
        heapq.heapify(heap)
        q = deque()
        time = 1
        while heap or q:
            print(heap,q,time)
            if not heap:
                print(heap)
                cnt,task,t = q.popleft()
                heapq.heappush(heap,[cnt,task])
                time = t
            while q and q[0][2]<=time:
                cnt,task,t = q.popleft()
                heapq.heappush(heap,[cnt,task])
            
            currentCnt,currentTask = heapq.heappop(heap)
            currentCnt +=1
            if currentCnt:
                q.append([currentCnt,currentTask,time+n+1])
            time +=1
        return time-1



        





    #     t = 1
    #     q.       maxHeap    
    #    []      [3-A,B-1,C-1]
    #    while q and q[-1][2] >= t:
    #     maxHeap.push([q.popleft()])
    #    if not heap:
    #     cnt,task,t = q.popleft()
    #    pop = 3-A
    #    2-A-4
        
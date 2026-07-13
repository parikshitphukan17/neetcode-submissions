
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        heap = []
        cnt = Counter(tasks)
        for k in cnt:
            heapq.heappush(heap,[-cnt[k],k])
        t = 1
        nextTasks = deque([])
        while heap or nextTasks:
            if not heap:
                task,time = nextTasks[0]
                t = time
            while nextTasks and nextTasks[0][1]<=t:
                task,time = nextTasks.popleft()
                heapq.heappush(heap,task)
            cnt,char = heapq.heappop(heap)
            cnt+=1
            if cnt<0:
                nextTasks.append([[cnt,char],t+n+1])
            if not heap and not nextTasks:
                return t
            t+=1
        









        
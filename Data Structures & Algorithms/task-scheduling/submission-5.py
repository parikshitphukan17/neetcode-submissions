class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        n+=1
        cnt = Counter(tasks)
        heap = []
        for k in cnt.keys():
            heapq.heappush(heap,[-cnt[k],k])
        cool = deque([])
        t = 1
        while cool or heap:
            print(t,cool,heap)
            if not heap and cool:
                t = cool[0][0]
            while cool and cool[0][0]<=t:
                time,c,k = cool.popleft()
                heapq.heappush(heap,[c,k])
            c,k = heapq.heappop(heap)
            if c+1<0:
                cool.append([t+n,c+1,k])
            t +=1
        return t-1

                


    #     A   A   A   B   C



    # [3A    B   C]



    # t = 1
    #     3A
    # t= 2
    # [5,2A]      [B,C]
    # [5,2A   6,B]    [C]
    # t =3
    # [5,2A   6,B  7,C]
    # t = 4 empty? get first value from nextGen = 5
    # t = 5



        
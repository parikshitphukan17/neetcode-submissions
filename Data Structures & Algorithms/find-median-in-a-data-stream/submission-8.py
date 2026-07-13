class MedianFinder:

    def __init__(self):
        self.max = []
        self.min = []
        

    def addNum(self, num: int) -> None:
        if not self.min or num<=self.min[0]:
            heapq.heappush(self.max,-num)
        else:
            heapq.heappush(self.min,num)
        if abs(len(self.max)-len(self.min))>1:
            if len(self.max)>len(self.min):
                heapq.heappush(self.min,-heapq.heappop(self.max))
            else:
                heapq.heappush(self.max,-heapq.heappop(self.min))
        



        

    def findMedian(self) -> float:
        if len(self.max) == len(self.min):
            return (self.min[0]-self.max[0])/2
        elif len(self.max)>len(self.min):
            return -self.max[0]
        else:
            return self.min[0]





        
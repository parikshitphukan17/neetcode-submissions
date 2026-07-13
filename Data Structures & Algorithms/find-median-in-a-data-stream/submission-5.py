class MedianFinder:

    def __init__(self):
        self.left = []
        self.right = []
        

    def addNum(self, num: int) -> None:
        if not self.right or num<= self.right[0]:
            heapq.heappush(self.left,-num)
        else:
            heapq.heappush(self.right,num)
        if len(self.left)-len(self.right) >=2:
            heapq.heappush(self.right,-heapq.heappop(self.left))
        if len(self.right)-len(self.left) >=2:
            heapq.heappush(self.left,-heapq.heappop(self.right))




        

    def findMedian(self) -> float:
        if len(self.left) == len(self.right):
            return (self.right[0] - self.left[0])/2
        elif len(self.left)>len(self.right):
            return -self.left[0]
        return self.right[0]



       


        
        
class MedianFinder:

    def __init__(self):
        self.left = []
        self.right = []
        

    def addNum(self, num: int) -> None:
        if not self.left or -self.left[0]>num:
            heapq.heappush(self.left,-num)
        else:
            heapq.heappush(self.right,num)
        if abs(len(self.left)-len(self.right)) > 1:
            if len(self.left)>len(self.right):
                heapq.heappush(self.right,-heapq.heappop(self.left))
            else:
                heapq.heappush(self.left,-heapq.heappop(self.right))
        

            
        

    def findMedian(self) -> float:
        if len(self.left) == len(self.right):
            return (-self.left[0]+self.right[0])/2
        elif len(self.left) > len(self.right):
            return -self.left[0]
        else:
            return self.right[0]
        
        
import heapq

class MedianFinder:

    def __init__(self):
        self.left = []
        self.right = []

        

        # [1,2,3,4,5,6]
        # [1,5,6,2,3,4]
        # l[].  [].   [1]
        # r[1]. [1,5]. [6]

        

    def addNum(self, num: int) -> None:
        if self.right and num<self.right[0]:
            heapq.heappush(self.left,-num)
        else:
            heapq.heappush(self.right,num)
        if len(self.left) -len(self.right)>1:
            heapq.heappush(self.right,-heapq.heappop(self.left))
        if len(self.right) - len(self.left)>1:
            heapq.heappush(self.left,-heapq.heappop(self.right))

            
            


        

    def findMedian(self) -> float:
        if len(self.left) == len(self.right):
            return (self.right[0] -self.left[0])/2
        if len(self.left)>len(self.right):
            return -self.left[0]
        return self.right[0]
        
        
        
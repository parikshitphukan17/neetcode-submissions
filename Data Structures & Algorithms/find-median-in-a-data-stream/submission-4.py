import heapq

class MedianFinder:

    def __init__(self):
        self.left = []
        self.right = []

        # [1,2,3] [4,5,6]
        # if eq max(left)+min(right)//2
        # if left>right max(left)
        # else min(right)

        # []   [1]
        # []   [1,2]
        # pop right append to left

        # [1,2,3,4,5,6]
        # [1,5,6,2,3,4]
        # l[].  [].   [1]
        # r[1]. [1,5]. [6]

        

    def addNum(self, num: int) -> None:
        if self.right and num<self.right[0]:
            heapq.heappush(self.left,-num)
        else:
            heapq.heappush(self.right,num)
        if len(self.left)-len(self.right)>1:
            heapq.heappush(self.right,-heapq.heappop(self.left))
        elif len(self.right)-len(self.left)>1:
            heapq.heappush(self.left,-heapq.heappop(self.right))

    

    def findMedian(self) -> float:
        print(self.left,self.right)
        if len(self.right) == len(self.left):
            return (self.right[0]-self.left[0])/2
        elif len(self.right)>len(self.left):

            return self.right[0]
        else:
            return -self.left[0]
        
        
        
        
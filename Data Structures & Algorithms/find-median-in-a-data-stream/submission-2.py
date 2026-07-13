import heapq
class MedianFinder:

    def __init__(self):
        self.small,self.large = [],[]
        

    def addNum(self, num: int) -> None:
        if self.large and num<self.large[0]:
            heapq.heappush(self.small,-num)
        else:
            heapq.heappush(self.large,num)
        if len(self.large) - len(self.small)>1:
            heapq.heappush(self.small,-heapq.heappop(self.large))
        if len(self.small) - len(self.large)>1:
            heapq.heappush(self.large,-heapq.heappop(self.small))

    

            

        

    def findMedian(self) -> float:
        if len(self.small) == len(self.large):
            return (self.large[0]-self.small[0])/2
        elif len(self.small)>len(self.large):
            return -self.small[0]
        return self.large[0]


        # [1,2,3,4,5,6,7,8]
        # 4,5,1,2,3,7,8,6
        # less [1,2,3,]
        # large [4,5,7]
        
        
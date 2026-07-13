class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        maxHeap = []
        minHeap = []

        l,r = 0,0
        res = 0
        while r<len(nums):
            heapq.heappush(maxHeap,[-nums[r],r])
            heapq.heappush(minHeap,[nums[r],r])
            # print(l,r,maxHeap,minHeap)
            while abs(-maxHeap[0][0]-minHeap[0][0])> limit:
                l+=1
                while maxHeap and  maxHeap[0][1] <l:
                    heapq.heappop(maxHeap)
                while minHeap and  minHeap[0][1] <l:
                    heapq.heappop(minHeap)
            res = max(res,r-l+1)
            r+=1
        return res
        
            


    #         l   r   r   r
    #     l   r
    #     10  1   2   4   7   2
    # max 10  10  2   4   7   
    # min 10  1   1   1   1

    
    
    # max.push([-val,i])
    # min.push([val,i])

    # if max-min > lim
    # move left till max -min  <= limit
    #     l ++ 
    #     and pop from max and min if l was max or min
    # res = r-l+1






        

        
        
import heapq

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap = []
        res = []
        for i,n in enumerate(nums):
            heapq.heappush(heap,[-n,i])
            print(i,heap,res)

            if (i+1)%k == 0 or len(res):
                while heap and heap[0][1] <= i-k:
                    heapq.heappop(heap)
                res.append(-heap[0][0])
        return res





        
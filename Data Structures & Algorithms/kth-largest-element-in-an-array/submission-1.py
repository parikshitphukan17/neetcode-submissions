import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = [-i for i in nums]
        heapq.heapify(heap)
        val = None
        while k>0:
            val = heapq.heappop(heap)
            k-=1
        return -val

        
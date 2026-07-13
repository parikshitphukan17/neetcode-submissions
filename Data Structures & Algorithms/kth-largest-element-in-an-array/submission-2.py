class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for n in nums:
            heapq.heappush(heap,-n)
        while True:
            val = heapq.heappop(heap)
            k -=1
            if not k:
                return -val

        
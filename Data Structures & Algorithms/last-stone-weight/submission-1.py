class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-i for i in stones]
        heapq.heapify(heap)
        while heap:
            large = -heapq.heappop(heap)
            if not heap:
                return large
            small = -heapq.heappop(heap)
            new = large -small
            if new:
                heapq.heappush(heap,-new)
        return 0

        
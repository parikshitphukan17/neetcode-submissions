import heapq

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        res = []
        for i,n in enumerate(nums):
            while q and nums[q[-1]] <=n:
                q.pop()
            q.append(i)
            while q and q[0]<=i-k:
                q.popleft()
            if i>=k-1:
                res.append(nums[q[0]])
        return res




        #  2 1
        # [1,2]
        # ans is first val
        #push and pop from right till value<=cur
        #pop from left till in window
        #res is first from left







        
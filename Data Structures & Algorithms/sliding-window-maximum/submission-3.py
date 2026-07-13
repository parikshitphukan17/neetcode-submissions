class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque([])
        res = []
        for i in range(len(nums)):
            while q and q[-1][1]<nums[i]:
                q.pop()
            q.append([i,nums[i]])
            if q[0][0] <=i-k:
                q.popleft()
            if i<k-1:
                continue
            res.append(q[0][1])
        return res  

        
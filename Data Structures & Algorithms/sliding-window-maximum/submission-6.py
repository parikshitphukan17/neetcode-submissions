class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        q = deque([])
        res =[]
        for i,n in enumerate(nums):
            while q and q[-1][1]<=n:
                q.pop()
            q.append([i,n])
            if i<k-1:
                continue
            if q[0][0]<=i-k:
                q.popleft()
            res.append(q[0][1])
        return res



        # [[1,2], [2,1],[3,0], []]

            
        # pop from right till greater value than current or empty
        # push
        # pop from left out of bound
        # 1st value is max
        # [2  1]


        # max is 0

        
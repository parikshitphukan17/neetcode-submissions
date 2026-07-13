class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque([])
        res = []
        for i in range(len(nums)):
            while q and q[-1][1]<nums[i]:
                q.pop()
            while q and q[0][0]<=i-k:
                q.popleft()
            q.append([i,nums[i]])
            if i<k-1:
                continue
            res.append(q[0][1])
        return res
             

    



        # if r<k-1:
        #     continue


        # [1,2,1]


        # pop till last val is not less than or empty then insert
        # pop from start till first val is in window

        # choose first val

        
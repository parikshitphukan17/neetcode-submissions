from bisect import bisect_left

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        tail = []
        for n in nums:
            i = bisect_left(tail,n)
            if i == len(tail):
                tail.append(n)
            else:
                tail[i] = n
        return len(tail)

        # N = len(nums)
        # dp = {}
        # def dfs(i,last):
        #     if i == N:
        #         return 0
            
        #     if (i,last) in dp:
        #         return dp[(i,last)]
            
        #     dp[(i,last)] = max(1 + dfs(i+1,nums[i]) if not last or last< nums[i] else 0,dfs(i+1,last))
        #     return dp[(i,last)]
        # return dfs(0,None)
            


            



        # [9,1,4,2,3,3,7]

        #  1,1,2,2,3,3,4

        
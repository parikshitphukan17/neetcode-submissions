class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        self.res = []
        l = len(nums)
        def dfs(i,cur):
            if(sum(cur) == target):
                self.res.append(cur.copy())
                return
            if (sum(cur)>target or i>=l):
                return
            cur.append(nums[i])
            dfs(i,cur)
            cur.pop()
            dfs(i+1,cur)
            
        dfs(0,[])
        return self.res


                        # [2,5,6,9]
                        # [2] []
                        # [2,2]. [2.5]

        
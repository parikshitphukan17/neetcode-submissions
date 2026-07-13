class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        N = len(nums)
        def dfs(i,cur):
            if i ==N:
                res.append(cur.copy())
                return
            cur.append(nums[i])
            dfs(i+1,cur)
            cur.pop()
            j = i+1
            while j<N and nums[j] == nums[i]:
                j +=1
            dfs(j,cur)
        dfs(0,[])
        return res
        
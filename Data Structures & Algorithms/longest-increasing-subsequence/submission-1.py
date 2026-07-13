class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        N = len(nums)
        self.s = 0
        def dfs(i,cur):
            if i == N:
                print(cur)
                self.s = max(self.s,len(cur))
                return
            if not cur or cur[-1]< nums[i]:
                cur.append(nums[i])
                dfs(i+1,cur)
                cur.pop()
                dfs(i+1,cur)
                return
            dfs(i+1,cur)
        dfs(0,[])
        return self.s
                
        
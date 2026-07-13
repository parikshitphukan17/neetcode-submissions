class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        cur,l=0,len(nums)
        nums.sort()
        while cur<l:
            i = cur+1
            j = l-1
            while i<j:
                s = nums[cur]+nums[i]+nums[j]
                #print(s,i,j,nums[i],nums[j])
                if s<0:
                    i+=1
                elif s>0:
                    j-=1
                else:
                    res.append([nums[cur],nums[i],nums[j]])
                    while i+1<l and nums[i] ==nums[i+1]:
                        i+=1
                    i+=1
                    while  j-1>=0 and nums[j] == nums[j-1]:
                        j-=1
                    j-=1

            while cur+1<l and nums[cur] == nums[cur+1]:
                cur+=1
            cur +=1
        return res
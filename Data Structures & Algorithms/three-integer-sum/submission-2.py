class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        cur,l=0,len(nums)
        nums.sort()
        while cur<l:
            i = cur+1
            j = l-1
            while i<j:
                print("cur ", nums[cur])
                s = nums[cur]+nums[i]+nums[j]
                #print(s,i,j,nums[i],nums[j])
                if s<0:
                    i+=1
                elif s>0:
                    j-=1
                    print("j-1 once ",j)
                else:
                    res.append([nums[cur],nums[i],nums[j]])
                    while i+1<l and nums[i] ==nums[i+1]:
                        i+=1
                        print("i+1",i)
                    i+=1
                    print("i",i)
                    while  j-1>=0 and nums[j] == nums[j-1]:
                        j-=1
                        print("j-1",j)
                    j-=1
                    print("j",j)
                print("after")
                #print(s,i,j,nums[i],nums[j])

            while cur+1<l and nums[cur] == nums[cur+1]:
                cur+=1
            cur +=1
            print("----")
        return res
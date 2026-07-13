class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt= {}
        bucket = []
        for i in nums:
            bucket.append([])
            cnt[i] = 1+cnt.get(i,0)
        for i in cnt.keys():
            bucket[cnt[i]-1].append(i)
        res = []
        for i in range(len(nums)-1,-1,-1):
            if k ==0 :
                return res
            if len(bucket[i])>0:
                for j in bucket[i]:
                    res.append(j)
                    k-=1
        return res
            






        
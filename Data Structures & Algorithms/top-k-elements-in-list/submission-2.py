class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        bucket = []
        res=[]
        for n in nums:
            count[n] = 1+ count.get(n,0)
            bucket.append([])
        for key in count.keys():
            bucket[count[key]-1].append(key)
        for i in range(len(nums)-1,-1,-1):
            if k ==0:
                return res
            if len(bucket[i])>0:
                for j in bucket[i]:
                    res.append(j)
                    k -=1
        return res
        

            
        
        
         
        
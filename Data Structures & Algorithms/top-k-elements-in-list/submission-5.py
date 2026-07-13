class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = defaultdict(int)
        bucket = []
        for n in nums:
            cnt[n] +=1
            bucket.append([])
        for c in cnt:
            bucket[cnt[c]-1].append(c)
        res = []
        for i in bucket[::-1]:
            for j in i:
                if k == 0:
                    return res
                res.append(j)
                k-=1

        return res  
        

        
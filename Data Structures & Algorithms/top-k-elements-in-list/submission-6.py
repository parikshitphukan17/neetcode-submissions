class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = Counter(nums)
        c = [[] for i in range(len(nums)+1)]
        for key in cnt:
            c[cnt[key]].append(key)
        
        res = []
        for i in range(len(nums),-1,-1):
            if not k:
                print(res)
                return res
            if c[i]:
                for r in c[i]:
                    res.append(r)
                    k-=1
                
        
        
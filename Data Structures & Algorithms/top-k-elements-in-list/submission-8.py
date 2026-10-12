class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        cnt = Counter(nums)
        buckets = defaultdict(list)
        for key in cnt.keys():
            buckets[cnt[key]].append(key)
        res = []
        for i in range(len(nums),-1,-1):
            if k == 0:
                return res
            if i in buckets:
                for n in buckets[i]:
                    if k == 0:
                        return res
                    res.append(n)
                    k -=1
        return res
        
        
        








        
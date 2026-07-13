class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        cur = [-1,-1,-1]
        t1,t2,t3 = target
        for a,b,c in triplets:
            if a<=t1 and b<=t2 and c<=t3:
                cur = [max(cur[0],a),max(cur[1],b),max(cur[2],c)]
        c1,c2,c3 = cur
        return c1==t1 and c2==t2 and c3 == t3
            
        
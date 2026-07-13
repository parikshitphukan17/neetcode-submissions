class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        cur = [-1,-1,-1]
        c1,c2,c3 = cur
        for n1,n2,n3 in triplets:
            if n1<= target[0] and n2<=target[1] and n3<=target[2]:
                cur = [max(c1,n1),max(c2,n2),max(c3,n3)]
                c1,c2,c3 = cur
        return c1== target[0] and c2==target[1] and c3==target[2]
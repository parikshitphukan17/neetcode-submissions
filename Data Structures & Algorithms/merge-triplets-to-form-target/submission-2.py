class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:

        cur = [-1,-1,-1]

        for a,b,c in triplets:
            if a<=target[0] and b<=target[1] and c<= target[2]:
                cur = [max(cur[0],a),max(cur[1],b),max(cur[2],c)]
            if cur[1] == target[1] and cur[2] == target[2] and cur[0] ==target[0]:
                return True
        return False
        
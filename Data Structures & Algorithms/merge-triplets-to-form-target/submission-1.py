class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        startPos = None
        
        for i in range(len(triplets)):
            n1,n2,n3 = triplets[i]
            if n1<=target[0] and n2<=target[1] and n3<= target[2]:
                startPos = i
                break
        
        if startPos is None:
            return False
        
        start = triplets[startPos]
        for i in range(startPos+1,len(triplets),1):
            n1,n2,n3 = triplets[i]
            if n1<=target[0] and n2<=target[1] and n3<= target[2]:
                start = [max(start[0],n1),max(start[1],n2),max(start[2],n3)]
            if start[0] == target[0] and start[1] == target[1] and start[2] == target[2]:
                return True
        if start[0] == target[0] and start[1] == target[1] and start[2] == target[2]:
                return True
        return False




        
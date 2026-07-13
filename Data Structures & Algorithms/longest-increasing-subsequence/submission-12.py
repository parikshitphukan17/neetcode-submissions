class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        prev = []
        res = 0
        for n in nums:
            cur = 0
            for i in range(len(prev)-1,-1,-1):
                if prev[i][0]<n:
                    cur = max(cur,prev[i][1])
            res = max(res,cur+1)
            prev.append([n,cur+1])
        return res
            

          
        # [[0,1]].      1
        # [[0,1],[1,2]]  0
        # [[0,1],[1,2],[0,1]].  3
        # [[0,1],[1,2],[0,1],[3,3]] 2
        # [[0,1],[1,2],[0,1],[3,3],[2,3]] 3
        # [[0,1],[1,2],[0,1],[3,3],[2,3],[3,4]]





        # [[9,1]].     1

        # [[1,1]].    4
        # [[1,1],[4,2]].  2
        # [[1,1],[2,2]]. 3
        # [[1,1],[2,2],[3,3]]. 3
        # [[1,1],[2,2],[3,3]]
        # [[1,1],[2,2],[7,4]]


        
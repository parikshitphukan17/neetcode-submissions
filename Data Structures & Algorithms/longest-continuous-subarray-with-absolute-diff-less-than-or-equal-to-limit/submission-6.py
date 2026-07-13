class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:




        maxQ = deque([])
        minQ = deque([])

        l,r = 0,0
        res = 0
        while r<len(nums):
            while maxQ and maxQ[-1][0]<nums[r]:
                maxQ.pop()
            while minQ and minQ[-1][0]>nums[r]:
                minQ.pop()
            maxQ.append([nums[r],r])
            minQ.append([nums[r],r])
            while maxQ[0][0] -minQ[0][0] >limit:
                l+=1
                while maxQ and maxQ[0][1]<l:
                    maxQ.popleft()
                while minQ and minQ[0][1]<l:
                    minQ.popleft()
            res = max(res,r-l+1)
            r+=1
        return res

        
            


            
    #     l   r
    #     10  1   2   4   7   2
    # max 10  1  
    # min 1

    #     1   2   4   7   2
    # max 1    
    # min 1
    # --
    # max 2    
    # min 1   2
    # --
    # max 4   
    # min 1   2   4

    # --
    # max 7
    # min 1   2   4   7

    # while max[0] -min[0] >limit:
    #     l+=1
    #     while max[0][1]<l:
    #         pop
    #     same with min




    
    
    # max.push([-val,i])
    # min.push([val,i])

    # if max-min > lim
    # move left till max -min  <= limit
    #     l ++ 
    #     and pop from max and min if l was max or min
    # res = r-l+1






        

        
        
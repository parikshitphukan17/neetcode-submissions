class MinStack:

    def __init__(self):
        self.stack = []
        self.min = float("inf")
        

    def push(self, val: int) -> None:
        if not self.stack:
            self.min = val
            self.stack.append(0)
            return
        self.stack.append(val -self.min)
        if val -self.min<=0:
            self.min = val
    



        
        

        

    def pop(self) -> None:
        val = self.stack.pop()
        if val<=0:
            self.min = self.min -val
        
        
        

        

    def top(self) -> int:
        if self.stack[-1]<=0:
            return self.min
        return self.stack[-1]+self.min

    
        

    def getMin(self) -> int:
        return self.min


    

# MinStack = []
# minVal = 0
#     15  4   8   7   3   2   6   1

# MinStack = [0] ,15
# MinStack = [0,-11] ,4
# MinStack = [0,-11,4] ,4
# MinStack = [0,-11,4,3] ,4
# MinStack = [0,-11,4,3,-1] ,3
# MinStack = [0,-11,4,3,-1,-1] ,2
# MinStack = [0,-11,4,3,-1,-1,4] ,2
# MinStack = [0,-11,4,3,-1,-1,4,-1] ,1


# if last <=0:
#     curMin = min
#     nextMin = 1 - last = 1- -1 = 2
# else:
#     curMin = min



















    



        15


        
        

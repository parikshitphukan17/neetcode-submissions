class MinStack:

    def __init__(self):
        self.minVal = -float("infinity")
        self.stack = []
        

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append(0)
            self.minVal = val
        else:
            self.stack.append(val-self.minVal)
            self.minVal = min(self.minVal,val)

        

    def pop(self) -> None:
        if not self.stack:
            return None
        last = self.stack.pop()
        if last<0:
            self.minVal = self.minVal - last

        

    def top(self) -> int:
        last = self.stack[-1]
        if last>=0:
            return last + self.minVal
        return self.minVal
        
        

    def getMin(self) -> int:
        return self.minVal
        

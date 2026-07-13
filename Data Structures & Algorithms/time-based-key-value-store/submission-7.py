class TimeMap:

    def __init__(self):
        self.tp = defaultdict(list)

        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.tp[key].append([value,timestamp])
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.tp:
            return ""
        arr = self.tp[key]
        l,r = 0,len(arr)-1
        res = ""
        while l<=r:
            m = (l+r)//2
            val,time = arr[m]
            if time<=timestamp:
                res=val
                if time ==timestamp:
                    return res
                l = m+1
            else:
                r = m-1
        return res





# ["alice"]
# "happy", 1

# "sad", 3


# find mid if less than 
#     poddible ans go right
#     if greater 
#     go left




        

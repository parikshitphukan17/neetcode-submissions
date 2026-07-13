class TimeMap:

    def __init__(self):

        self.timestamps = defaultdict(list)





        # 1,3,5,7 6-> 5

        # if m== target:
        #     return
        # if m<target:
        #     res = m


        

    def set(self, key: str, value: str, timestamp: int) -> None:
        
        self.timestamps[key].append((timestamp,value))
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timestamps:
            return ""
        row = self.timestamps[key]
        l,r = 0,len(row)-1
        res = ""
        while l<=r:
            m = (l+r)//2
            curT,curV = row[m]
            if curT ==  timestamp:
                return curV
            if curT<timestamp:
                res = curV
                l = m+1
            else:
                r = m-1
        return res
        

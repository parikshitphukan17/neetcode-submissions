class TimeMap:

    def __init__(self):
        self.timeMap = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timeMap[key].append([timestamp,value])
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timeMap:
            return ""
        row = self.timeMap[key]
        l,r = 0,len(row)-1
        res = None
        while l<=r:
            m = (l+r)//2
            if row[m][0]< timestamp:
                l = m+1
                res = row[m]
            elif row[m][0]>timestamp:
                r =m-1
            else:
                res = row[m]
                break
        return res[1] if res else ""
        

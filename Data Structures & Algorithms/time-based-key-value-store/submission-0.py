class TimeMap:

    def __init__(self):
        self.mapping = defaultdict(list)

        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.mapping[key].append([timestamp,value])
        

    def get(self, key: str, timestamp: int) -> str:
        if self.mapping[key] == []:
            return ""
        row = self.mapping[key]
        l,r = 0,len(row)-1
        res = ""
        while l<=r:
            m = l+r
            if row[m][0]>timestamp:
                r = m-1
            elif row[m][0]<timestamp:
                res = row[m][1]
                l = m+1
            else:
                return row[m][1]
        return res



        

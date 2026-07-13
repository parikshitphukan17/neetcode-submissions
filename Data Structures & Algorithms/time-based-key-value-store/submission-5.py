class TimeMap:

    def __init__(self):
        self.map = defaultdict(list)

        
        # if less than <:
        #     pos ans and move right if less else retyrb

        # else :
        #     move left
        #         m.   
        # hp,1 sd,3.  ts,4.  tq,5
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key].append([value,timestamp])


        
        

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        if key not in self.map:
            return res
        row = self.map[key]
        l,r = 0,len(row)-1
        while l<=r:
            m = (l+r)//2
            if row[m][1]<=timestamp:
                res = row[m][0]
                if row[m][1] == timestamp:
                    return res
                l = m+1
            else:
                r = m-1
        return res



        

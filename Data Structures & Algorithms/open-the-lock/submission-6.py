class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        q = deque([])
        q.append(target)
        vis = set()
        for dead in deadends:
            vis.add(dead)
        vis.add(target)
        res = 0

        def addNei(val,next):
            for i in range(len(val)):
                for j in range(2):
                    c = int(val[i])-1 if j==0 else int(val[i])+1
                    if c<0:
                        c = 9
                    elif c>9:
                        c =0 
                    nei = val[:i]+str(c)+val[i+1:]

                    if nei in vis:
                        continue
                    vis.add(nei)
                    next.append(nei)
        



        while q:
            next = deque([])
            while q:
                cur = q.popleft()
                if cur == "0000":
                    return res
                addNei(cur,next)
            res +=1
            
            q = next
        return -1
                





        
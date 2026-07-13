class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        def part(sub,cur):
            if not sub:
                if cur:
                    res.append(cur.copy())
                return
            curSub = ""
            for i in range(len(sub)):
                curSub += sub[i]
                if (curSub == curSub[::-1]):
                    cur.append(str(curSub))
                    part(sub[i+1:],cur)
                    cur.pop()
        part(s,[])
        return res


        
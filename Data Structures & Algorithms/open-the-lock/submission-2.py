class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if "0000" in deadends:
            return -1
        q = deque(["0000"])
        res = 0
        vis = set()
        vis.add("0000")
        while q:
            child = deque()
            while q:
                cur = q.popleft()
                if cur == target:
                    return res
                for i in range(len(cur)):
                    digit = int(cur[i])
                    digit1 = digit+1 if digit <9 else 0
                    digit2 = digit-1 if digit >0 else 9

                    childCur = cur[:i]+ str(digit1) + cur[i+1:]
                    if childCur not in deadends and childCur not in vis:
                        child.append(childCur)
                        vis.add(childCur)
                    childCur = cur[:i]+ str(digit2) + cur[i+1:]
                    if childCur not in deadends and childCur not in vis:
                        child.append(childCur)
                        vis.add(childCur)
            q =child
            res +=1
        return -1
        

        